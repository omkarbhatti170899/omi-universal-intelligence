MODES = {
    "personal":{"label":"Personal Omi","description":"Everyday questions, planning, organization and life assistance.","tools":["memory","planning"]},
    "student":{"label":"Student Omi","description":"Learning, explanations, study plans, practice and research.","tools":["memory","research","files"]},
    "professional":{"label":"Professional Omi","description":"Documents, meetings, analysis, reports and workplace workflows.","tools":["files","research","planning"]},
    "enterprise":{"label":"Enterprise Omi","description":"Governed organizational intelligence, workflows and analytics.","tools":["files","research","analytics","audit"]},
    "manager":{"label":"Manager Intelligence","description":"Operational briefs, exceptions, trends and action planning.","tools":["analytics","reports","audit"]},
    "developer":{"label":"Developer Omi","description":"Code, debugging, architecture, testing and deployment assistance.","tools":["code","files","testing"]},
    "creator":{"label":"Creator Omi","description":"Writing, scripts, concepts, creative development and content workflows.","tools":["writing","files","creative"]},
    "researcher":{"label":"Research Omi","description":"Evidence-oriented research, source comparison and synthesis.","tools":["research","files","citations"]},
}
ALIASES={"work":"professional","study":"student","business":"enterprise","code":"developer","creative":"creator","research":"researcher"}

def resolve(mode):
    key=ALIASES.get(str(mode).lower(),str(mode).lower())
    return key if key in MODES else "personal"

def all_modes():
    return MODES
