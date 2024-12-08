import sys

def get_ans_coords():
    f = open("ex_ans.txt", "r")
    orig_lines = []
    coords = []
    for i, line in enumerate(f):
        for j, c in enumerate(line):
            if c == "#":
                coords.append((i,j))
    return coords

def read_file():
    f = open(sys.argv[1] if len(sys.argv) > 1 else "ex.txt", "r")
    orig_lines = []
    for line in f:
        orig_lines.append(line.strip())
    f.close()
    return orig_lines


def problem_1():
    lines = read_file()
    antennas = {}
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c != '.':
                if c in antennas:
                    antennas[c].append((i, j))
                else:
                    antennas[c] = [(i, j)]
    antinodes = set()
    for antenna in antennas:
        print(antenna)
        coords = antennas[antenna]
        print(coords)
        for a in coords:
            for b in coords:
                if a == b:
                    continue
                print(a)
                print(b)
                a_r, a_c = a
                b_r, b_c = b
                p1_c, p2_c, p1_r, p2_r = None, None, None, None
                antinodes.add(a)
                antinodes.add(b)
                if a_r <= b_r and a_c <= b_c:
                    p1_r = a_r - abs(b_r - a_r)
                    p1_c = a_c - abs(b_c - a_c)
                    p2_r = b_r + abs(b_r - a_r)
                    p2_c = b_c + abs(b_c - a_c)
                    while p1_c >= 0 and p1_r >= 0 and p1_r < len(lines) and p1_c < len(lines[0]):
                        antinodes.add((p1_r, p1_c))
                        p1_r = p1_r - abs(b_r - a_r)
                        p1_c = p1_c - abs(b_c - a_c)
                    while p2_c >= 0 and p2_r >= 0 and p2_r < len(lines) and p2_c < len(lines[0]):
                        antinodes.add((p2_r, p2_c))
                        p2_r = p2_r + abs(b_r - a_r)
                        p2_c = p2_c + abs(b_c - a_c)
                elif b_r <= a_r and b_c <= a_c:
                    p1_r = b_r - abs(b_r - a_r)
                    p1_c = b_c - abs(b_c - a_c)
                    p2_r = a_r + abs(b_r - a_r)
                    p2_c = a_c + abs(b_c - a_c)
                    while p1_c >= 0 and p1_r >= 0 and p1_r < len(lines) and p1_c < len(lines[0]):
                        antinodes.add((p1_r, p1_c))
                        p1_r = p1_r - abs(b_r - a_r)
                        p1_c = p1_c - abs(b_c - a_c)
                    while p2_c >= 0 and p2_r >= 0 and p2_r < len(lines) and p2_c < len(lines[0]):
                        antinodes.add((p2_r, p2_c))
                        p2_r = p2_r + abs(b_r - a_r)
                        p2_c = p2_c + abs(b_c - a_c)
                elif a_r <= b_r and a_c >= b_c:
                    p1_r = a_r - abs(b_r - a_r)
                    p1_c = a_c + abs(b_c - a_c)
                    p2_r = b_r + abs(b_r - a_r)
                    p2_c = b_c - abs(b_c - a_c)
                    while p1_c >= 0 and p1_r >= 0 and p1_r < len(lines) and p1_c < len(lines[0]):
                        antinodes.add((p1_r, p1_c))
                        p1_r = p1_r - abs(b_r - a_r)
                        p1_c = p1_c + abs(b_c - a_c)
                    while p2_c >= 0 and p2_r >= 0 and p2_r < len(lines) and p2_c < len(lines[0]):
                        antinodes.add((p2_r, p2_c))
                        p2_r = p2_r + abs(b_r - a_r)
                        p2_c = p2_c - abs(b_c - a_c)
                else:
                    p1_r = b_r - abs(b_r - a_r)
                    p1_c = b_c + abs(b_c - a_c)
                    p2_r = a_r + abs(b_r - a_r)
                    p2_c = a_c - abs(b_c - a_c)
                    while p1_c >= 0 and p1_r >= 0 and p1_r < len(lines) and p1_c < len(lines[0]):
                        antinodes.add((p1_r, p1_c))
                        p1_r = p1_r - abs(b_r - a_r)
                        p1_c = p1_c + abs(b_c - a_c)
                    while p2_c >= 0 and p2_r >= 0 and p2_r < len(lines) and p2_c < len(lines[0]):
                        antinodes.add((p2_r, p2_c))
                        p2_r = p2_r + abs(b_r - a_r)
                        p2_c = p2_c - abs(b_c - a_c)
                
    print(len(antinodes))

    ans = []
    for i, line in enumerate(lines):
        line_arr = list(line)
        for j, c in enumerate(line_arr):
            if (i,j) in antinodes and c == '.':
                line_arr[j] = '#'
        print(''.join(line_arr))
        
        

problem_1()