import os,sys
os.environ["OMI_PROVIDER"]="mock"
sys.path.insert(0,"backend")
from providers import get_provider, OpenAIResponsesProvider
p=get_provider()
assert p.name=="mock"
assert p.generate("hello")["model"]=="local-safe"
# Verify live provider refuses missing secrets instead of silently misbehaving.
os.environ.pop("OMI_AI_API_KEY",None)
try:
    OpenAIResponsesProvider()
    raise AssertionError("missing API key should fail closed")
except RuntimeError:
    pass
print("V12 provider contract: PASS")
