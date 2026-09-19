import sys,urllib.request,json,threading,os,tempfile
os.environ["OMI_PROVIDER"]="mock"; os.environ["OMI_DB"]=tempfile.mktemp(suffix=".db")
sys.path.insert(0,"backend")
from manager_intelligence import build_brief,roi_template
b=build_brief({"cases_assisted":10},[])
assert b["title"]=="Omi Executive Brief" and b["highlights"][0]["value"]==10
assert "estimated_savings" in roi_template()
print("MANAGER INTELLIGENCE: PASS")
