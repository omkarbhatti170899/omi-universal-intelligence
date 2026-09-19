from pathlib import Path
import os, sys
root=Path(__file__).resolve().parents[1]
assert (root/'.env.example').exists()
assert (root/'.gitignore').exists()
assert (root/'web/manifest.webmanifest').exists()
assert (root/'web/sw.js').exists()
html=(root/'web/index.html').read_text()
assert 'manifest.webmanifest' in html
assert 'serviceWorker' in html
sys.path.insert(0,str(root/'backend'))
os.environ['OMI_PROVIDER']='mock'
from server import Handler
assert Handler.server_version == 'Omi/1.0'
print('Product packaging: PASS')
