import re

with open('input.txt') as txt:
    stack, moves = txt.read().split('\n\n')

lines = []
for line in stack.splitlines():
    if line[1].isdigit():
        continue
    else:
        pattern = re.compile(r'(.{3})\s')
        lines.append(re.findall(pattern, line) + [line[-3:]])

stacks = [[] for idx in range(len(lines[0]))]
for line in lines:
    for idx, container in enumerate(line):
        crate_id = container[1]
        if not crate_id.isspace():
            stacks[idx].insert(0, crate_id)

instr = []
for move in moves.splitlines():
    instr.append([int(s) for s in re.findall(r'\b\d+\b', move)])

# delete reversed function for part 2
for qty, start, end in instr:
    transfer = list(reversed(stacks[start-1][-qty:]))
    stacks[start-1] = stacks[start-1][:-qty]
    stacks[end-1] += transfer
    print(stacks)
    print()

print("".join([stack[len(stack)-1] for stack in stacks]))