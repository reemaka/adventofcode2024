import math
import sys
from functools import cache

# 0
# 1
# 2024
# 20 24
# 2 0 2 4
# 4048 1 4048 8096
# 40 48 2024 40 48 80 96
# 4 0 4 8 20 24 4 0 4 8 8 0 9 6

def read_file():
    f = open(sys.argv[1] if len(sys.argv) > 1 else "ex.txt", "r")
    l = f.readline()
    f.close()
    return l.strip()

def has_even_digits(num):
    count = 0
    while num > 0:
        num = int(num / 10)
        count += 1
    return count % 2 == 0

@cache
def calc(num_iters, num):
    if (num_iters == 0):
        return 1
    
    num_iters -= 1
    if num == 0:
        return calc(num_iters, 1)
    elif has_even_digits(num):
        num_str = str(num)
        l = int(len(num_str) / 2)
        num1 = int(num_str[:l])
        num2 = int(num_str[l:])
        return calc(num_iters, num1) + calc(num_iters, num2)
    return calc(num_iters, num * 2024) 
        
@cache
def p2():
    line = read_file()
    nums = list(map(int, line.split(' ')))
    sum = 0
    for num in nums:
        sum += calc(75, num)
    print(sum)
    
def calc_len(num_iters, nums):
    
    for i in range(num_iters):
        new = []
        for num in nums:
            if num == 0:
                new.append(1)
                continue
            if len(str(num)) % 2 == 0:
                num_str = str(num)
                l = int(len(num_str) / 2)
                num1 = num_str[:l]
                num2 = num_str[l:]
                new.append(int(num1))
                new.append(int(num2))
                continue
            new.append(num * 2024)
        nums = new
    return len(nums) 

def p1():
    line = read_file()
    nums = list(map(int, line.split(' ')))
    print(calc_len(25, nums))

p1()
p2()