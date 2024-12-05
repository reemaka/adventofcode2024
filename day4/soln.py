import sys
from enum import Enum

f = open(sys.argv[1] if len(sys.argv) > 1 else "ex.txt", "r")
lines = []
for line in f:
    lines.append(line.strip())
f.close()

class Direction(Enum):
    LEFT=1
    RIGHT=2
    UP=3
    DOWN=4
    UP_LEFT=5
    UP_RIGHT=6
    DOWN_LEFT=7
    DOWN_RIGHT=8

def get_next_indices(i, j, dir):
    if dir == Direction.LEFT:
        return i - 1, j
    elif dir == Direction.RIGHT:
        return i + 1, j
    elif dir == Direction.UP:
        return i, j - 1
    elif dir == Direction.DOWN:
        return i, j + 1
    elif dir == Direction.UP_LEFT:
        return i - 1, j - 1
    elif dir == Direction.UP_RIGHT:
        return i + 1, j - 1
    elif dir == Direction.DOWN_LEFT:
        return i - 1, j + 1
    elif dir == Direction.DOWN_RIGHT:
        return i + 1, j + 1

# PART 1
def check(term, i, j, grid, dir):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return False
    if len(term) == 1:
        return grid[i][j] == term
    if grid[i][j] == term[0]:
        t = term[1:]
        next_i, next_j = get_next_indices(i, j, dir)
        return check(t, next_i, next_j, grid, dir)
    return False

def check_iterative(term, i, j, grid, dir):
    while term:
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return False
        if len(term) == 1:
            return grid[i][j] == term
        if grid[i][j] == term[0]:
            term = term[1:]
            i, j = get_next_indices(i, j, dir)
        else:
            return False
    return False

count = 0
for i, row in enumerate(lines):
    for j, col in enumerate(row):
        for dir in Direction:
            if check('XMAS', i, j, lines, dir):
                count += 1
print(count)


# PART 2
backwards_slash_a_indices = set()
forwards_slash_a_indices = set()
for i, row in enumerate(lines):
    for j, col in enumerate(row):
        # Find all instances of MAS that contribute to the \ shape in the X and
        # add the index of their 'A's to the list.
        for dir in [Direction.UP_LEFT, Direction.DOWN_RIGHT]:
            if check('MAS', i, j, lines, dir):
                backwards_slash_a_indices.add(get_next_indices(i, j, dir))
        # Find all instances of MAS that contribute to the / shape in the X and
        # add the index of their 'A's to the list.
        for dir in [Direction.DOWN_LEFT, Direction.UP_RIGHT]:
            if check('MAS', i, j, lines, dir):
                forwards_slash_a_indices.add(get_next_indices(i, j, dir))

# Count the number of \ and / shapes that intersect at their 'A' char.
print(len(list(filter(lambda b: b in forwards_slash_a_indices, backwards_slash_a_indices))))