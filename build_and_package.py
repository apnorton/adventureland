import base64
import os
import shutil
import subprocess
import sys
from pathlib import Path

from jinja2 import Template

if len(sys.argv) < 2:
    print("USAGE: python build_and_package.py [project_folder]")
    sys.exit(1)

project = Path(sys.argv[1])
os.chdir(project)

target_folder = Path("./pkg/")

# first do a little cleanup
if target_folder.exists():
    shutil.rmtree(target_folder)

# Build the js (has exports, tho, so we'll do some sketchy substitution)
subprocess.run(["wasm-pack", "build", "--release", "--target", "web"])

potential_wasm_files = list(target_folder.glob("*_bg.wasm"))
assert len(potential_wasm_files) == 1

wasm_file = potential_wasm_files[0]
with open(wasm_file, "rb") as f:
    wasm_data = f.read()

wasm_encoded = base64.b64encode(wasm_data).decode("utf-8")

potential_js_files = list(target_folder.glob("*.js"))
assert len(potential_js_files) == 1

js_file = potential_js_files[0]
with open(js_file) as f:
    js_lines = f.read().splitlines()

# Ultra-hacky time --- we can't put exports in here, so we either remove export labels on
# functions or delete the whole line if it's the other two exports in the generated code.
# Really, really hacky.
for i in range(len(js_lines)):
    line = js_lines[i]
    if line.strip().startswith("export function"):
        js_lines[i] = line.replace("export ", "")
    elif line.strip().startswith("export"):
        js_lines[i] = "//delete this"
js_lines = filter(lambda s: s != "//delete this", js_lines)

os.chdir("..")
with open("bot_template.js.j2") as f:
    template = Template(f.read())

rendered = template.render(wasm_encoded=wasm_encoded, generated_js="\n".join(js_lines))
with open("bot_code.js", "w") as f:
    f.write(rendered)
