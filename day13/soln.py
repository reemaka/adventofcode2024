import sys 
import math

def read_file():
    f = open(sys.argv[1] if len(sys.argv) > 1 else "ex.txt", "r")
    lines = []
    for line in f:
        lines.append(line.strip())
    f.close()
    return lines

def get_x_y_for_btn(line):
    a_x, a_y = line.split(':')[1].split(',')
    a_x = int(a_x.split('+')[1])
    a_y = int(a_y.split('+')[1])
    return a_x, a_y

def get_prize_x_y(line):
    prize_x, prize_y = line.split(':')[1].split(',')
    prize_x = int(prize_x.split('=')[1])
    prize_y = int(prize_y.split('=')[1])
    return prize_x, prize_y

def calc_btn_presses(a_x, a_y, b_x, b_y, prize_x, prize_y):
    min_cost = None
    for a_i in range(100):
        for b_i in range(100):
            loc_x = a_i * a_x + b_i * b_x
            loc_y = a_i * a_y + b_i * b_y
            if loc_x == prize_x and loc_y == prize_y:
                cost = 3 * a_i + b_i
                if not min_cost or cost < min_cost:
                    min_cost = cost
                break
            elif loc_x > prize_x or loc_y > prize_y:  
                continue
    return min_cost

def p1():
    lines = read_file()

    i = 0
    min_cost = 0
    while i < len(lines):
        a_x, a_y = get_x_y_for_btn(lines[i])
        b_x, b_y = get_x_y_for_btn(lines[i+1])
        prize_x, prize_y = get_prize_x_y(lines[i+2])
        cost = calc_btn_presses(a_x, a_y, b_x, b_y, prize_x, prize_y)
        if cost:
            min_cost += cost
        i += 4
    
    print(min_cost)

def calc_a_b_clicks(a_x, a_y, b_x, b_y, prize_x, prize_y):
    a_i = (b_x * prize_y - b_y * prize_x) / (b_x * a_y - b_y * a_x)
    b_i = (prize_y - a_i * a_y) / b_y
    if b_i.is_integer() and a_i.is_integer():
        return 3 * a_i + b_i
    else:
        return None
        
def p2():
    lines = read_file()

    i = 0
    min_cost = 0
    while i < len(lines):
        a_x, a_y = get_x_y_for_btn(lines[i])
        b_x, b_y = get_x_y_for_btn(lines[i+1])
        prize_x, prize_y = get_prize_x_y(lines[i+2])
        prize_x += 10000000000000
        prize_y += 10000000000000
        cost = calc_a_b_clicks(a_x, a_y, b_x, b_y, prize_x, prize_y)
        if cost:
            min_cost += cost
        i += 4
    
    print(min_cost)   

p1()
p2()