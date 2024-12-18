import sys

registers = {"A": 0, "B": 0, "C": 0}
instr_ptr = 0
output = []

def read_file():
  f = open(sys.argv[1] if len(sys.argv) > 1 else "ex.txt", "r")
  lines = []
  for line in f:
    lines.append(line.strip())
  f.close()
  return lines

def get_init_reg_val(line):
    return int(line.split(':')[1])

def get_prog(line):
    return list(map(int, line.split(':')[1].split(',')))

def eval_combo(combo):
    if 0 <= combo <= 3:
        return combo
    elif combo == 4:
        return registers["A"]
    elif combo == 5:
        return registers["B"]
    elif combo == 6:
        return registers["C"]
    
def adv(combo):
    numerator = registers["A"]
    denominator = 2 ** eval_combo(combo)
    registers["A"] = int(numerator / denominator)
    global instr_ptr
    instr_ptr += 2

def bxl(lit):
    registers["B"] = registers["B"] ^ lit
    global instr_ptr
    instr_ptr += 2

def bst(combo):
    registers["B"] = eval_combo(combo) % 8
    global instr_ptr
    instr_ptr += 2

def jnz(lit):
    global instr_ptr
    if registers["A"] == 0:
        instr_ptr += 2
        return
    
    instr_ptr = lit

def bxc(unused):
    registers["B"] = registers["B"] ^ registers["C"]
    global instr_ptr
    instr_ptr += 2
    
def out(combo):
    global instr_ptr, output
    to_output = eval_combo(combo) % 8
    output.append(str(to_output))
    instr_ptr += 2

def bdv(combo):
    numerator = registers["A"]
    denominator = 2 ** eval_combo(combo)
    registers["B"] = int(numerator / denominator)
    global instr_ptr
    instr_ptr += 2

def cdv(combo):
    numerator = registers["A"]
    denominator = 2 ** eval_combo(combo)
    registers["C"] = int(numerator / denominator)
    global instr_ptr
    instr_ptr += 2

instructions = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}

def p1():
    f = read_file()
    registers["A"] = get_init_reg_val(f[0])
    registers["B"] = get_init_reg_val(f[1])
    registers["C"] = get_init_reg_val(f[2])

    prog = get_prog(f[4])

    global instr_ptr
    i = 0
    while (instr_ptr < len(prog) - 1):
        instructions[prog[instr_ptr]](prog[instr_ptr + 1])
    print(','.join(output))

p1()