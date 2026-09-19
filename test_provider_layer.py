import sys, os
sys.path.insert(0, 'backend')
import providers
p = providers.get_provider()
assert p.name == os.getenv('OMI_PROVIDER', 'mock')
assert p.generate('test', 'fast')['provider'] == p.name
print('Provider adapter smoke test: PASS')
