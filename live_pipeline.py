from providers import get_provider, ProviderError
from planner import plan
from conversation import history, add

def execute(question, session_id="default", mode="auto"):
    p=plan(question,mode)
    ctx=history(session_id)
    provider=get_provider()
    result=provider.generate(question,ctx,p.get("route","auto"))
    add(session_id,"user",question)
    add(session_id,"assistant",result["text"])
    return {"plan":p,"result":result,"context_turns":len(ctx)}

def health():
    return {"provider":get_provider().name,"live_configured":get_provider().name!="mock"}
