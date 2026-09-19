import json, os, urllib.request, urllib.error
from model_router import choose

class ProviderError(RuntimeError): pass

class Provider:
    name="base"
    def generate(self, prompt, context=None, mode="auto"):
        raise NotImplementedError

class MockProvider(Provider):
    name="mock"; model="local-safe"
    def generate(self,prompt,context=None,mode="auto"):
        return {"text":"Omi received your request and completed its local planning and verification flow. Configure a live provider for generation.","provider":self.name,"model":self.model}

class OpenAIResponsesProvider(Provider):
    name="openai"
    def __init__(self):
        self.base_url=os.getenv("OMI_AI_BASE_URL","https://api.openai.com/v1").rstrip("/")
        self.api_key=os.getenv("OMI_AI_API_KEY","")
        self.model=os.getenv("OMI_AI_MODEL","")
        if not self.api_key: raise ProviderError("OMI_AI_API_KEY is not configured")
    def generate(self,prompt,context=None,mode="auto"):
        parts=[]
        for item in (context or []):
            if item.get("role") in {"user","assistant"} and item.get("content"):
                parts.append({"role":item["role"],"content":str(item["content"])[:6000]})
        parts.append({"role":"user","content":str(prompt)[:12000]})
        payload={"model":self.model,"input":parts}
        data=json.dumps(payload).encode()
        req=urllib.request.Request(
            self.base_url+"/responses",data=data,
            headers={"Authorization":"Bearer "+self.api_key,"Content-Type":"application/json"},
            method="POST")
        try:
            with urllib.request.urlopen(req,timeout=45) as response:
                result=json.loads(response.read())
        except urllib.error.HTTPError as e:
            detail=e.read().decode("utf-8","replace")[:500]
            raise ProviderError(f"OpenAI API HTTP {e.code}: {detail}") from e
        except (urllib.error.URLError,TimeoutError) as e:
            raise ProviderError("OpenAI API connection failed") from e
        text=result.get("output_text")
        if not text:
            # Defensive fallback for compatible Responses API implementations.
            chunks=[]
            for item in result.get("output",[]):
                for content in item.get("content",[]):
                    if isinstance(content,dict) and content.get("text"):
                        chunks.append(content["text"])
            text="\n".join(chunks).strip()
        if not text: raise ProviderError("Provider returned no text")
        return {"text":str(text),"provider":self.name,"model":self.model}

def get_provider():
    selected=os.getenv("OMI_PROVIDER","mock").strip().lower()
    return OpenAIResponsesProvider() if selected in {"openai","openai_responses"} else MockProvider()
