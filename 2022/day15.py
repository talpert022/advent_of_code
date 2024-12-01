import re

with open('input.txt') as txt:
    sensors = txt.read().splitlines()

print("Here")
sbs = [list(map(int, re.findall(r'=(-*\d+)', sb))) for sb in sensors]
min_x, max_x = min(*[sb[0] for sb in sbs], *[sb[2] for sb in sbs]), max(*[sb[0] for sb in sbs], *[sb[2] for sb in sbs])
min_y, max_y = min(*[sb[1] for sb in sbs], *[sb[3] for sb in sbs]), max(*[sb[1] for sb in sbs], *[sb[3] for sb in sbs])

# construct tunnels 2d array and keep track of x and y offsets for points
print("Here")
tunnels = [['.' for _ in range(min_x, max_x+1)] for _ in range(min_y, max_y+1)]
print("Not Here :(")
# place S and B coordinates onto tunnles using offsets
for sx, sy, bx, by in sbs:
    print(sx, sy, bx, by)
    tunnels[sy-min_y][sx-min_x] = 'S'
    tunnels[by-min_y][bx-min_x] = 'B'

# for each S, convert any dot point within the manhattan distance from S to B to a #
for sx, sy, bx, by in sbs:

    print(sx, sy, bx, by)
    # calculate manhattan distance from S to B
    md = abs(sx - bx) + abs(sy - by)

    # Calculate coordinates relative to tunnels array
    sxr, syr, bxr, byr = sx-min_x, sy-min_y, bx-min_x, by-min_y

    # loop over the 2d slice from (xs - md -> xs + md, ys - md -> ys + md) that is not out of bounds of tunnels
    for i in range(syr - md, syr + md + 1):
        for j in range(sxr - md, sxr + md + 1):
            if 0 <= i < len(tunnels) and 0 <= j < len(tunnels[0]):
            # Any point <= md in that slice convert to #, except S or B points
                if abs(sx - j) + abs(sy - i) <= md and tunnels[i][j] == '.':
                    tunnels[i][j] = '#'
            
no_beacon_points = 0
for x in tunnels[10 - min_y]:
    if x == '#':
        no_beacon_points += 1

print(no_beacon_points)