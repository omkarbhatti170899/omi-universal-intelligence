import sys, os
sys.path.insert(0,'backend')
import research
assert not research._allowed('example.com')
try: research.fetch('http://example.com')
except research.ResearchError: pass
else: raise AssertionError('HTTP URL must be blocked')
print('Research security smoke test: PASS')
