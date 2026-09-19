import os,sys
os.environ["OMI_PROVIDER"]="mock"
sys.path.insert(0,"backend")
from live_pipeline import execute
a=execute("Explain Omi","s1","auto")
assert a["result"]["provider"]=="mock"
assert a["plan"]["route"]
b=execute("Continue that","s1","auto")
assert b["context_turns"]>=2
print("LIVE PIPELINE: PASS")
