import sys

def read_file():
    f = open(sys.argv[1] if len(sys.argv) > 1 else "ex.txt", "r")
    orig_lines = []
    for line in f:
        orig_lines.append(line.strip())
    f.close()
    return orig_lines

def get_ans_coords():
    f = open("ex_ans.txt", "r")
    orig_lines = []
    coords = []
    for i, line in enumerate(f):
        for j, c in enumerate(line):
            if c == "#":
                coords.append((i,j))
    return coords

def in_bounds(c, r, lines):
    return c >= 0 and r >= 0 and r < len(lines) and c < len(lines[0])

def print_antinodes(antinodes, lines):
    ans = []
    for i, line in enumerate(lines):
        line_arr = list(line)
        for j, c in enumerate(line_arr):
            if (i,j) in antinodes and c == '.':
                line_arr[j] = '#'
        print(''.join(line_arr))

def calc_antinodes_count():
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
        for j in coords:
            for z in coords:
                if j == z:
                    continue
                if j[1] < z[1]:
                    a = j
                    b = z
                else:
                    b = j
                    a = z

                antinodes.add(a)
                antinodes.add(b)
                    
                a_r, a_c = a
                b_r, b_c = b
                p1_c, p2_c, p1_r, p2_r = None, None, None, None
                delta_r = abs(b_r - a_r)
                delta_c = abs(b_c - a_c)
                if a_r <= b_r:
                    p1_r = a_r - delta_r
                    p1_c = a_c - delta_c
                    while in_bounds(p1_c, p1_r, lines):
                        antinodes.add((p1_r, p1_c))
                        p1_r = p1_r - delta_r
                        p1_c = p1_c - delta_c
                    p2_r = b_r + delta_r
                    p2_c = b_c + delta_c
                    while in_bounds(p2_c, p2_r, lines):
                        antinodes.add((p2_r, p2_c))
                        p2_r = p2_r + delta_r
                        p2_c = p2_c + delta_c
                else:
                    p1_r = b_r - delta_r
                    p1_c = b_c + delta_c
                    while in_bounds(p1_c, p1_r, lines):
                        antinodes.add((p1_r, p1_c))
                        p1_r = p1_r - delta_r
                        p1_c = p1_c + delta_c
                    p2_r = a_r + delta_r
                    p2_c = a_c - delta_c
                    while in_bounds(p2_c, p2_r, lines):
                        antinodes.add((p2_r, p2_c))
                        p2_r = p2_r + delta_r
                        p2_c = p2_c - delta_c
                
    print(len(antinodes))
    print_antinodes(antinodes, lines)

calc_antinodes_count()