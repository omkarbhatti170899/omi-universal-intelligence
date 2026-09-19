import os,sys,tempfile
os.environ['OMI_PROVIDER']='mock'
sys.path.insert(0,'backend')
import orchestrator
result, source=orchestrator.run('test orchestration','fast')
assert result['provider']=='mock' and source is None
print('Orchestrator smoke test: PASS')
