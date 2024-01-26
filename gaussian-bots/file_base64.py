import base64
import sys

if len(sys.argv) < 2:
    print("USAGE: python base64.py [FILENAME]")

filename = sys.argv[1]
print(filename)

with open(filename, "rb") as f:
    print(base64.b64encode(f.read()).decode("utf-8"))