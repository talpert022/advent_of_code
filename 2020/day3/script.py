from functools import reduce

with open('input.txt') as txt:
    input = txt.read().splitlines()

def trees_hit(h, v):
    x = y = 0
    trees = 0
    while y < len(input) - 1:
        x += h
        y += v

        # correcting for extended horizontal space
        if x >= len(input[y]):
            x %= len(input[y])

        if input[y][x] == '#':
            trees += 1
    
    return trees

print(reduce(lambda x,y: x*y, [trees_hit(h,v) for h,v in [(1,1), (3,1), (5,1), (7,1), (1,2)]]))

