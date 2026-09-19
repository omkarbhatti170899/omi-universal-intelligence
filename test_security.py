import os, sys, tempfile
os.environ['OMI_DB']=tempfile.mktemp(suffix='.db')
sys.path.insert(0,'backend')
import security
uid=security.create_user('test@example.com','correct-horse-battery')
tok=security.login('test@example.com','correct-horse-battery')
assert tok and security.user_from_token(tok)==uid
assert security.login('test@example.com','wrong-password') is None
security.remember(uid,'user prefers brief descriptions')
assert security.memories(uid)[0]['content']=='user prefers brief descriptions'
assert security.can_use_tool(uid,'provider_generate')
assert not security.can_use_tool(uid,'arbitrary_shell')
print('Security + memory smoke test: PASS')
