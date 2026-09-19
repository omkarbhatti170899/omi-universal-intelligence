import re

TASK_PATTERNS = {
    "research": r"\b(latest|recent|news|research|sources?|verify|compare)\b",
    "code": r"\b(code|debug|program|api|repository|deploy|software)\b",
    "analysis": r"\b(analy[sz]e|analysis|calculate|evaluate|break down|why)\b",
    "creative": r"\b(write|rewrite|poem|story|design|creative)\b",
}

def classify(question):
    q=question.lower()
    hits=[name for name,pat in TASK_PATTERNS.items() if re.search(pat,q)]
    return hits or ["general"]

def choose_route(question, requested="auto"):
    if requested and requested!="auto": return requested
    kinds=classify(question)
    if "research" in kinds: return "research"
    if "code" in kinds or "analysis" in kinds: return "deep"
    if "creative" in kinds: return "fast"
    return "auto"

def plan(question, requested="auto"):
    route=choose_route(question, requested)
    kinds=classify(question)
    steps=["understand request"]
    if route=="research": steps += ["retrieve approved evidence","separate evidence from instructions"]
    if route=="deep": steps += ["decompose task","reason through constraints"]
    steps += ["generate response","run verification","return brief description"]
    return {"route":route,"task_types":kinds,"steps":steps[:6]}
