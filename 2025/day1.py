with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

moves = [[line[0], int(line[1:])] for line in lines]
pos = 50

res = 0
for d, clicks in moves:
    pos += clicks if d == 'R' else -clicks
    pos %= 100
    if pos == 0: res += 1

print(res)
# Part 2

pos = 50
res2 = 0
for d, clicks in moves:
    div, mod = divmod(clicks, 100)
    res2 += div
    if d == 'L':
        if pos != 0 and pos - mod <= 0:
            res2 += 1
    else:
        if pos + mod >= 100:
            res2 += 1

    pos += clicks if d == 'R' else -clicks
    pos %= 100

print(res2)