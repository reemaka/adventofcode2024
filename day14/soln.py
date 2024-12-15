import sys 
import math
from PIL import Image

def read_file():
    f = open(sys.argv[1] if len(sys.argv) > 1 else "ex.txt", "r")
    lines = []
    for line in f:
        lines.append(line.strip())
    f.close()
    return lines

def print_grid(filename, width, height, robot_positions):
    im = Image.new('RGB', (101, 103), "black")
    pixels = im.load()
    for y in range(height):
        for x in range(width):
            if (x, y) in robot_positions:
                pixels[x,y] = (0, 255, 0)

    im.save(filename)
    

def p1(seconds, width, height):
    f = read_file()
    positions = []
    q1, q2, q3, q4 = 0, 0, 0, 0
    for line in f:
        pos, vel = line.split(' ')
        pos = list(map(int, pos.split('=')[1].split(',')))
        vel = list(map(int, vel.split('=')[1].split(',')))

        next_pos_x = (pos[0] + vel[0] * seconds) % width
        next_pos_y = (pos[1] + vel[1] * seconds) % height
        positions.append((next_pos_x, next_pos_y))

        if next_pos_x == math.floor(width / 2):
            continue
        if next_pos_y == math.floor(height / 2):
            continue
        if next_pos_x < width / 2:
            if next_pos_y < height / 2:
                q1 += 1
            else:
                q3 += 1
        else:
            if next_pos_y < height / 2:
                q2 += 1
            else:
                q4 += 1
    return q1 * q2 * q3 * q4, positions

def p2(seconds, width, height):
    min_danger = None
    for i in range(seconds + 1):
        # Force skipping this index because it's a min but not the tree
        if i == 1120:
            continue
        danger, positions = p1(i, width, height)
        if not min_danger or danger < min_danger:
            min_danger = danger
            print_grid("imgs/" + str(i) + ".jpg", width, height, positions)
                
print(p1(100, 101, 103)[0])
p2(10000, 101, 103)