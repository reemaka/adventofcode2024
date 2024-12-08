import sys
import copy

f = open(sys.argv[1] if len(sys.argv) > 1 else "ex.txt", "r")
orig_lines = []
for line in f:
    orig_lines.append(list(line.strip()))
f.close()

start = None
for i, line in enumerate(orig_lines):
    for j, cell in enumerate(line):
        if cell == "^":
            start = (i, j)

# PART 1
lines = copy.deepcopy(orig_lines)
i, j = start
dir = "^"
while i >= 0 and j >= 0 and i < len(lines) and j < len(lines[0]):
    lines[i][j] = "X"
    if dir == "^":
        i -= 1
    elif dir == ">":
        j += 1
    elif dir =="v":
        i += 1
    elif dir == "<":
        j -= 1
    if i >= 0 and j >= 0 and i < len(lines) and j < len(lines[0]):
        if lines[i][j] == "#":
            if dir == "^":
                i += 1
                dir = ">"
            elif dir == ">":
                j -= 1
                dir = "v"
            elif dir == "v":
                i -= 1
                dir = "<"
            elif dir == "<":
                j += 1
                dir = "^"

count = 0
for line in lines:
    for cell in line:
        if cell == "X":
            count += 1
print(count)


# PART 2
def transform(i, j, dir):
    if dir == "^":
        i -= 1
    elif dir == ">":
        j += 1
    elif dir =="v":
        i += 1
    elif dir == "<":
        j -= 1
    return (i, j)

def in_bounds(i, j, grid):
    return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])
    
def print_grid(grid):
    for k, blah in enumerate(grid):
        print(''.join(blah), k, i, j)
    print('\n')

rotations_map = {"^": ["^", ">", "v", "<"],
             ">": [">", "v", "<", "^"],
             "v": ["v", "<", "^", ">"],
             "<": ["<", "^", ">", "v"]}

def check_for_cycle_3(grid):
    i, j = start
    dir = grid[i][j]
    visited = set()
    while in_bounds(i, j, grid):
        coord = (i, j, dir)

        if coord in visited:
            return True
        visited.add(coord)
        
        rotations = rotations_map[dir]
        for r in rotations:
            next_i, next_j = transform(i, j, r)
            if not in_bounds(next_i, next_j, grid):
                return False
            if grid[next_i][next_j] != '#':
                i = next_i
                j = next_j
                dir = r
                break

cycles = []
c2 = 0
copy_lines = copy.deepcopy(orig_lines)
i, j = start
for r, l in enumerate(copy_lines):
    for c, cl in enumerate(l):
        if r == i and c == j:
            continue
        if orig_lines[r][c] != '.':
            continue
        new_lines = copy_lines
        new_lines[r][c] = "#"
        if check_for_cycle_3(new_lines):
            cycles.append((r, c))
            c2 += 1
        new_lines[r][c] = "."

print(c2)