import sys
def read_file():
    f = open(sys.argv[1] if len(sys.argv) > 1 else "ex.txt", "r")
    lines = []
    for line in f:
        lines.append(list(map(int, list(line.strip()))))
    f.close()
    return lines

def can_reach(i, j, visited, lines, curr):
    if i < 0 or j < 0 or i >= len(lines) or j >= len(lines[0]):
        return set()
    if (i, j) in visited:
        return set()
    visited.add((i,j))
    if curr == 9 and lines[i][j] == 9:
        return {(i, j)} 

    if curr != lines[i][j]:
        return set()
    
    curr += 1
    all = can_reach(i - 1, j, visited.copy(), lines, curr) 
    all |= can_reach(i + 1, j, visited.copy(), lines, curr)
    all |= can_reach(i, j - 1, visited.copy(), lines, curr)
    return all | can_reach(i, j + 1, visited.copy(), lines, curr)
    

def can_reach_2(i, j, visited, lines, curr):
    if i < 0 or j < 0 or i >= len(lines) or j >= len(lines[0]):
        return 0
    if (i, j) in visited:
        return 0
    visited.add((i,j))
    if curr == 9 and lines[i][j] == 9:
        return 1

    if curr != lines[i][j]:
        return 0
    
    curr += 1
    sum = can_reach_2(i - 1, j, visited.copy(), lines, curr)
    sum += can_reach_2(i + 1, j, visited.copy(), lines, curr)
    sum += can_reach_2(i, j - 1, visited.copy(), lines, curr)
    return sum + can_reach_2(i, j + 1, visited.copy(), lines, curr)
 
def p2():
    sum = 0
    lines = read_file()
    for i, line in enumerate(lines):
        for j, cell in enumerate(line):
            if cell == 0:
                visited = set()
                visited.add((i, j))
                sum += can_reach_2(i - 1, j, visited.copy(), lines, 1)
                sum += can_reach_2(i + 1, j, visited.copy(), lines, 1)
                sum += can_reach_2(i, j - 1, visited.copy(), lines, 1)
                sum += can_reach_2(i, j + 1, visited.copy(), lines, 1)
    print(sum)

   
def p1():
    sum = 0
    lines = read_file()
    for i, line in enumerate(lines):
        for j, cell in enumerate(line):
            if cell == 0:
                visited = set()
                visited.add((i, j))
                indices = can_reach(i - 1, j, visited.copy(), lines, 1)
                indices |= can_reach(i + 1, j, visited.copy(), lines, 1)
                indices |= can_reach(i, j - 1, visited.copy(), lines, 1)
                indices |= can_reach(i, j + 1, visited.copy(), lines, 1)
                sum += len(indices)
    print(sum)

                    

p1()
p2()