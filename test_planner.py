import sys
sys.path.insert(0,'backend')
from planner import plan
p=plan('Compare the latest AI research and verify sources.')
assert p['route']=='research'
assert 'retrieve approved evidence' in p['steps']
p=plan('Debug this Python API.')
assert p['route']=='deep'
print('Planner smoke test: PASS')
