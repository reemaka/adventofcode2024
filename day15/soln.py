import sys 

def read_file():
    f = open(sys.argv[1] if len(sys.argv) > 1 else "ex.txt", "r")
    grid_over = False
    grid = []
    moves = []
    for line in f:
        if line == "\n":
            grid_over = True
            continue
        
        if not grid_over:
            grid.append(list(line.strip()))
        else:
            moves.extend(list(line.strip()))
            
    f.close()
    return grid, moves

def print_grid(grid):
    for line in grid:
        print(''.join(line))

def get_next_indices(i, j, dir):
    if dir == "<":
        return i, j - 1
    elif dir == ">":
        return i, j + 1
    elif dir == "^":
        return i - 1, j
    elif dir == "v":
        return i + 1, j

def in_bounds(grid, i, j):
    return i > 0 and i < len(grid) - 1 and j > 0 and j < len(grid[0]) - 1

def run_sim(grid, i, j, moves):
    print(i, j)
    
    while len(moves) > 0:
        m = moves[0]
        next_i, next_j = get_next_indices(i, j, m)
        if not in_bounds(grid, next_i, next_j):
            moves = moves[1:]
        elif grid[next_i][next_j] == ".":
            grid[i][j] = "."
            grid[next_i][next_j] = "@"
            i, j, moves = (next_i, next_j, moves[1:])
        elif grid[next_i][next_j] == "O":
            empty_i, empty_j = next_i, next_j
            found = False
            while in_bounds(grid, empty_i, empty_j):
                if grid[empty_i][empty_j] == "#":
                    break
                if grid[empty_i][empty_j] == ".":
                    found = True
                    break
                empty_i, empty_j = get_next_indices(empty_i, empty_j, m)
            if found:
                grid[empty_i][empty_j] = "O"
                grid[next_i][next_j] = "@"
                grid[i][j] = "."
                i, j, moves = (next_i, next_j, moves[1:])
            else:
                moves = moves[1:]
        elif grid[next_i][next_j] == "#":
            moves = moves[1:]

def calc_gps_sum(grid):
    sum = 0
    for i, line in enumerate(grid):
        for j, cell in enumerate(line):
            if cell == "O":
                sum += i * 100 + j
    print(sum)

            
def p1():
    grid, moves = read_file()

    found = False
    for i, line in enumerate(grid):
        for j, cell in enumerate(line):
            if cell == "@":
                run_sim(grid, i, j, moves)
                print_grid(grid)
                found = True
                break
        if found:
            break
    calc_gps_sum(grid)
        

p1()