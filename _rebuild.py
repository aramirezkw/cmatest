#!/usr/bin/env python3
"""Re-encode _template_src.html back into the agenticoverlay.html bundle.
Leaves the manifest (fonts/assets) untouched. Replicates the original
encoder: JSON-encode the template string, then escape '</' as '<\\u002F'
so an embedded </script> can't break out of the bundle's script tag."""
import re, json, sys

BUNDLE, SRC = 'agenticoverlay.html', '_template_src.html'
with open(BUNDLE) as f: html = f.read()
with open(SRC) as f: tmpl = f.read()

payload = json.dumps(tmpl, ensure_ascii=False).replace('</', '<\\u002F')
pat = re.compile(r'(<script type="__bundler/template">)(.*?)(</script>)', re.S)
if not pat.search(html): sys.exit("template tag not found")
html = pat.sub(lambda m: m.group(1) + '\n' + payload + '\n  ' + m.group(3), html, count=1)
# Write the canonical bundle and the GitHub Pages entry point (index.html) in lockstep.
for out in (BUNDLE, 'index.html'):
    with open(out, 'w') as f: f.write(html)
print("rebuilt", BUNDLE, "+ index.html | payload chars:", len(payload))
