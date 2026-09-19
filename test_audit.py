import sys, tempfile, os, json
os.environ['OMI_AUDIT_LOG']=tempfile.mktemp()
sys.path.insert(0,'backend')
import audit
audit.event('test', 'user-1', route='fast', provider='mock', outcome='ok')
line=open(os.environ['OMI_AUDIT_LOG']).read()
d=json.loads(line)
assert d['kind']=='test' and d['user_id']=='user-1' and 'question' not in d
print('Audit-log privacy smoke test: PASS')
