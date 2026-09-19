from providers import get_provider
def snapshot():
    p=get_provider()
    return {"provider":p.name,"configured":p.name=="mock" or bool(__import__("os").getenv(p.name.upper()+"_API_KEY"))}
