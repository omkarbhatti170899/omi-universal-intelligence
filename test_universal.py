import sys
sys.path.insert(0,"backend")
from universal_modes import resolve,all_modes
from universal_router import route
from localization import profile
from capabilities import get_capabilities
assert resolve("work")=="professional"
assert resolve("code")=="developer"
assert "manager" in all_modes()
assert route("student")["mode"]=="student"
assert profile("Hindi","Asia/Kolkata","INR")["currency"]=="INR"
assert get_capabilities()["multilingual"] is True
print("UNIVERSAL INTELLIGENCE: PASS")
