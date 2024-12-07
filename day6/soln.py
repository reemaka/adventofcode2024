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

def change_dir(dir):
    dirs = {"^": ">", ">": "v", "v": "<", "<": "^"}
    return dirs[dir]

def in_bounds(i, j, grid):
    return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])
    
def get_sym_for_dir(dir):
    if dir == ">" or dir == "<":
        return "-"
    else:
        return "|"

def sym_matches_for_dir(dir, sym):
    if dir == ">" or dir == "<":
        return sym == "-" or sym == "+"
    else:
        return sym == "|" or sym == "+"

def print_grid(grid):
    for k, blah in enumerate(grid):
        print(''.join(blah), k, i, j)
    print('\n')
    
# don't ready any of this, it doesn't work
def check_for_cycle_2(grid):
    curr_pos = start
    curr_i, curr_j = curr_pos
    curr = grid[curr_i][curr_j]
    dir = "^"

    first = True
    while in_bounds(curr_i, curr_j, grid):
        # print_grid(grid)

        next_pos = transform(curr_i, curr_j, dir)
        next_i, next_j = next_pos
        if not in_bounds(next_i, next_j, grid):
            return False
        next = grid[next_i][next_j]

        if curr == ".":
            if next == "#":
                grid[curr_i][curr_j] = "+"
                dir = change_dir(dir)
                next_i, next_j = transform(curr_i, curr_j, dir)
                if not in_bounds(next_i, next_j, grid):
                    return False
                next = grid[next_i][next_j]
            else:
                grid[curr_i][curr_j] = get_sym_for_dir(dir)
        elif curr == "-" and get_sym_for_dir(dir)== "|" or curr == "|" and get_sym_for_dir(dir) == "-":
            grid[curr_i][curr_j] = "+"
            if next == "#":
                return True
        if next == "+":
            return True
        if sym_matches_for_dir(dir, next) and (curr == "+" or (curr == "^" and not first)): 
            return True

            
        curr_pos = transform(curr_i, curr_j, dir)
        curr_i, curr_j = curr_pos
        curr = grid[curr_i][curr_j]
        first = False
    
    return False

    
# works for example input but not real input
def check_for_cycle(grid):
    i, j = start
    dir = "^"
    first = True
    while in_bounds(i, j, grid):
        # print_grid(grid)
        orig_i = i
        orig_j = j
        i, j = transform(i,j,dir)
        if not in_bounds(i, j, grid):
            return False
        next = grid[i][j]

        if next == "#":
            i = orig_i
            j = orig_j
            if dir == "^":
                dir = ">"
            elif dir == ">":
                dir = "v"
            elif dir == "v":
                dir = "<"
            elif dir == "<":
                dir = "^"
            i, j = transform(i, j, dir)
            next = grid[i][j]

            curr = grid[orig_i][orig_j]
            if sym_matches_for_dir(dir, next) and (curr == "+" or (curr == "^" and not first)): 
                return True
            grid[orig_i][orig_j] = "+"
        elif orig_i != start[0] or orig_j != start[1]:
            if dir == ">" or dir == "<":
                grid[orig_i][orig_j] = "-"
            else:
                grid [orig_i][orig_j] = "|"
        first = False
    return False
    

cycles = []
c2 = 0
copy_lines = copy.deepcopy(orig_lines)
i, j = start
for r, l in enumerate(copy_lines):
    for c, cl in enumerate(l):
        print(r,c)
        if r == i and c == j:
            continue
        if orig_lines[r][c] != '.':
            continue
        new_lines = copy.deepcopy(orig_lines)
        new_lines[r][c] = "#"
        if check_for_cycle(new_lines):
            cycles.append((r, c))
            c2 += 1

print(cycles)
print(c2)