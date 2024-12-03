import sys
import re

f = open(sys.argv[1] if len(sys.argv) > 1 else "ex.txt", "r")

lines = ""
for l in f:
    lines += l

matches = re.findall(r'(mul\(\d{1,3},\d{1,3}\))', lines)
ans = 0
for match in matches:
    l, r = match.split('(')[1].split(',')
    r = int(r[:-1])
    l = int(l)
    ans += r * l
print(ans)

matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', lines)
ans = 0
enabled = True
for match in matches:
    if match == "do()":
        enabled = True
        continue
    elif match == "don't()":
        enabled = False
        continue
    if not enabled:
        continue
    l, r = match.split('(')[1].split(',')
    r = int(r[:-1])
    l = int(l)
    ans += r * l
print(ans)

