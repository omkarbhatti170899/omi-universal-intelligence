import sys
sys.path.insert(0,'backend')
import limits
assert limits.allow('test-client')
print('Rate-limit smoke test: PASS')
