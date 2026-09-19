import time, statistics

def build_brief(metrics=None, events=None):
    metrics=metrics or {}
    events=events or []
    highlights=[]
    for k,v in metrics.items():
        if isinstance(v,(int,float)):
            highlights.append({"metric":k,"value":v})
    recent=events[-20:]
    return {
        "title":"Omi Executive Brief",
        "generated_at":int(time.time()),
        "summary":"Omi has converted the available operational signals into a concise management brief.",
        "highlights":highlights,
        "recent_events":recent,
        "next_actions":[
            "Review the highest-impact exception first.",
            "Validate unusual trends against the underlying source data.",
            "Assign an owner and due date to confirmed issues."
        ],
        "disclaimer":"Operational impact and savings should be calculated from verified business data; Omi does not invent ROI figures."
    }

def roi_template(metrics=None):
    m=metrics or {}
    return {
        "hours_saved":m.get("hours_saved",0),
        "cases_assisted":m.get("cases_assisted",0),
        "automation_rate":m.get("automation_rate",0),
        "estimated_savings":m.get("estimated_savings",None),
        "note":"Estimated savings must be based on an approved internal cost model."
    }
