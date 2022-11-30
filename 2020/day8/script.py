import re

with open('input.txt') as txt:
    input = txt.read()

instructions = re.findall(r'([a-z]+) ([+-])(\d+)', input)
print(instructions)

def run(instructions):
    accumulator = 0
    idx = 0
    vis = []
    while idx not in vis and 0 <= idx < len(instructions):
        instr, sign, arg = instructions[idx]
        vis.append(idx)
        if instr == 'acc':
            accumulator += int(arg) if sign == '+' else -(int(arg))
            idx += 1
        elif instr == 'jmp':
            idx += int(arg) if sign == '+' else -(int(arg))
        else:
            idx += 1

    return idx == len(instructions), accumulator

# part 1

# print(run(instructions)[1])

# part 2

for idx in range(len(instructions)):
    orig = instructions[idx]
    instr, sign, arg = orig

    if instr == 'jmp':
       new_instr = 'nop', sign, arg
    elif instr == 'nop':
        new_instr = 'jmp', sign, arg
    else: 
        continue
    
    instructions[idx] = new_instr

    finished, acc = run(instructions)
    if finished:
        print(acc)
        break
    else:
        instructions[idx] = orig



