import sys
while True:
    text=input()
    if text[-1]=="?":
        print("Quack!",flush=True)
    elif text[-1]==".":
        print("*Nod*",flush=True)
    elif text=="I quacked the code!":
        break
    sys.stdout.flush()
"""
import sys

for line in sys.stdin:
    text = line.strip()
    if text.endswith("?"):
        print("Quack!")
    elif text.endswith("."):
        print("*Nod*")
    elif text == "I quacked the code!":
        break
"""