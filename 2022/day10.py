with open('input.txt') as txt:
    instructions = txt.read().splitlines()

x = 1
cycle = 1

def check_strength(cycle, val):
    if cycle in [20,60,100,140,180,220]:
        return cycle*val
    else:
        return 0

r = 0
for instr in instructions:
    if instr == 'noop':
        cycle += 1
    else:
        cycle += 1
        r += check_strength(cycle,x)
        cycle += 1
        x += int(instr.split()[1])
    r += check_strength(cycle, x)

print(r)

# part 2

display = ['' for _ in range(6)]
x = 1
cycle = 1

def draw_display(cycle, x):
    row = (cycle-1) // 40
    lit = [x-1, x, x+1]
    current_pixel = (cycle % 40) - 1
    if current_pixel in lit:
        display[row] += (' # ')
    else:
        display[row] += (' . ')

for instr in instructions:
    if instr == 'noop':
        draw_display(cycle, x)
    else:
        draw_display(cycle, x)
        cycle += 1
        draw_display(cycle, x)
        x += int(instr.split()[1])
    cycle += 1

for row in display:
    print(row)
