import sys
from functools import cmp_to_key

f = open(sys.argv[1] if len(sys.argv) > 1 else "ex.txt", "r")
lines = []
for line in f:
    lines.append(line.strip())
f.close()

i = 0
rules = {}
while "|" in lines[i]:
    a, b = lines[i].split("|")
    a = int(a)
    b = int(b)
    if b in rules:
        rules[b].add(a)
    else:
        val = set()
        val.add(a)
        rules[b] = val
    i += 1

updates = []
while i < len(lines):
    if lines[i]:
        pages = list(map(int, lines[i].split(",")))
        updates.append(pages)
    i += 1

def are_pages_correctly_ordered(rules, pages):
    seen = set()
    cannot_see = set()
    is_correct = True
    for page in pages:
        seen.add(page)
        if page in cannot_see:
            is_correct = False
            break
        if page in rules and not rules[page] in seen:
            for val in rules[page]:
                cannot_see.add(val)
    return is_correct

# PART 1
ans = 0
for pages in updates:
    if are_pages_correctly_ordered(rules, pages):
        ans += pages[int(len(pages) / 2)]
print(ans)

# PART 2
def compare_page(a, b):
    if b in rules and a in rules[b]:
        return -1
    elif a in rules and b in rules[a]:
        return 1
    else:
        return 0
        
ans = 0
for pages in updates:
    if not are_pages_correctly_ordered(rules, pages):
        sorted_pages = sorted(pages, key=cmp_to_key(compare_page))
        ans += sorted_pages[int(len(sorted_pages) / 2)]
print(ans)