import re

with open('input.txt') as txt:
    rocklines = txt.read().splitlines()

# deconstruct rocklines into arrays of coordinate tuples
rocks = [[tuple(map(int, pair)) for pair in re.findall(r'(\d+),(\d+)', rock)] for rock in rocklines]

# find lowest and highest x and highest y coordinates
min_x, max_x, max_y = float('inf'), float('-inf'), float('-inf')
for rock in rocks:
    for x,y in rock:
        min_x = min(x, min_x)
        max_x = max(x, max_x)
        max_y = max(y, max_y)

# construct 2d array of dots from these numbers
X_OFFSET = 10000
cave = [['.' for _ in range(min_x-X_OFFSET, max_x+X_OFFSET)] for _ in range(max_y + 3)]

# draw rock lines from each previous to next coordinates for each structure
for rock in rocks:
    prev_x, prev_y = rock[0]
    for x,y in rock[1:]:
        if x == prev_x:             # vertical rock line
            cx = x - min_x + X_OFFSET
            if prev_y > y:
                for a in range(y, prev_y+1):
                    cave[a][cx] = '#'
            else:
                for a in range(prev_y, y+1):
                    cave[a][cx] = '#'
        else:                       # horizontal rock line
            if prev_x > x:
                for a in range(x, prev_x+1):
                    cx = a - min_x + X_OFFSET
                    cave[y][cx] = '#'
            else:
                for a in range(prev_x, x+1):
                    cx = a - min_x + X_OFFSET
                    cave[y][cx] = '#'
        prev_x, prev_y= x,y

# draw floor for part 2, delete for part 1
for x in range(len(cave[0])):
    cave[max_y + 2][x] = '#'

# simulate one grain of sand falling until it rests and draw it there until sand hits bottom of array
sand_entry = 500 - min_x + X_OFFSET
num_sands = 0
while True:
    sand_x, sand_y = sand_entry,0
    while True:
        if cave[sand_y + 1][sand_x] == '.':
            sand_y += 1
        elif cave[sand_y + 1][sand_x-1] == '.':
            sand_x, sand_y = sand_x-1, sand_y+1
        elif cave[sand_y+1][sand_x+1] == '.':
            sand_x, sand_y = sand_x+1, sand_y+1
        else:
            cave[sand_y][sand_x] = '*'
            break
    num_sands += 1 # Ctrl-x, ctrl-v this line at line 66 for part 1
    if (sand_x, sand_y) == (sand_entry,0):
        break
    
print(num_sands)
