from universal_modes import resolve, MODES
from model_router import choose

def route(mode="personal", complexity=0, tools=False):
    m=resolve(mode)
    tier,model=choose("auto",complexity=complexity,tools=tools)
    return {"mode":m,"mode_info":MODES[m],"tier":tier,"model":model}
