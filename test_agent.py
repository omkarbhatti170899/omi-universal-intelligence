import sys, os
os.environ['OMI_AUDIT_LOG']='/tmp/omi_agent_test.jsonl'
sys.path.insert(0,'backend')
from agent import execute
r=execute('Analyze this code and explain the problem.','auto','u1')
assert r['execution']['status']=='ready'
assert len(r['execution']['steps']) <= 6
assert r['next_action']=='provider_generation'
print('Agent execution smoke test: PASS')
