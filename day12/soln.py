import sys 

def read_file():
    f = open(sys.argv[1] if len(sys.argv) > 1 else "ex.txt", "r")
    lines = []
    for line in f:
        lines.append(list(line.strip()))
    f.close()
    return lines

def calc_area(grid, visited, i, j, label):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return set()
    if label != grid[i][j]:
        return set()
    if (i, j) in visited:
        return set()

    visited.add((i, j))
    area = set()
    area.add((i,j))
    area |= calc_area(grid, visited, i - 1, j, label)
    area |= calc_area(grid, visited, i + 1, j, label)
    area |= calc_area(grid, visited, i, j - 1, label)
    area |= calc_area(grid, visited, i , j + 1, label) 
    return area

def calc_perim(grid, region, label):
    perim = 0
    for i, j in region:
        perim += 4
        if i - 1 >= 0 and grid[i-1][j] == label:
            perim -= 1
        if j - 1 >= 0 and grid[i][j-1] == label:
            perim -= 1
        if i + 1 < len(grid) and grid[i+1][j] == label:
            perim -= 1
        if j + 1 < len(grid[0]) and grid[i][j+1] == label:
            perim -= 1
    return perim

def calc_sides(grid, region, label):
    top_sides = set()
    left_sides = set()
    bottom_sides = set()
    right_sides = set()
    for i, j in region:
        if i - 1 < 0 or grid[i-1][j] != label:
            top_sides.add((i-1, i))
        if j - 1 < 0 or grid[i][j-1] != label:
            left_sides.add((j-1, j))
        if i + 1 >= len(grid) or grid[i + 1][j] != label:
            bottom_sides.add((i+1,i))
        if j + 1 >= len(grid[0]) or grid[i][j+1] != label:
            right_sides.add((j,j+1))
    return len(top_sides) + len(left_sides) + len(bottom_sides) + len(right_sides)

def p1():
    lines = read_file()

    sum = 0
    area_visited = set()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            region = calc_area(lines, area_visited, i, j, c)
            perim = calc_perim(lines, region, c)
            sum += len(region) * perim
    print(sum)

def p2():
    lines = read_file()

    sum = 0
    area_visited = set()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            region = calc_area(lines, area_visited, i, j, c)
            sides = calc_sides(lines, region, c)
            sum += len(region) * sides
    print(sum)

p1()
p2()