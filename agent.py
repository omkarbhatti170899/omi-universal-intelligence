from planner import plan
from audit import event

class AgentError(RuntimeError): pass

MAX_STEPS=6

def execute(question, requested="auto", user_id=None):
    p=plan(question,requested)
    steps=p["steps"][:MAX_STEPS]
    completed=[]
    for step in steps:
        # The agent records intent/execution stages; actual privileged actions remain
        # behind explicit tool adapters and security policy.
        completed.append({"step":step,"status":"planned"})
        event("agent_step",user_id,route=p["route"],outcome="planned",
              meta={"step":step})
    return {"plan":p,"execution":{"status":"ready","steps":completed},
            "next_action":"provider_generation"}
