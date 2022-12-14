from collections import deque
import math

with open('input.txt') as txt:
    heights = txt.read().splitlines()

def find_shortest_path(start, heights):
    pathsteps = deque([(start, 0)])
    vis = set()
    while pathsteps:
        cord, steps = pathsteps.popleft()
        height = heights[cord[0]][cord[1]] if heights[cord[0]][cord[1]] != 'S' else 'a'

        if height == 'E':
            return steps

        for x,y in [(0,1), (1,0), (-1,0), (0,-1)]:
            nc = (cord[0]+x, cord[1]+y)
            if nc not in vis and (nc[0] >= 0 and nc[0] < len(heights) \
                and nc[1] >= 0 \
                and nc[1] < len(heights[0])):
                    nh = heights[nc[0]][nc[1]] if heights[nc[0]][nc[1]] != 'E' else 'z'
                    if ord(nh) <= ord(height) + 1: # nc are eligible for path according to requirements
                        vis.add(nc)
                        pathsteps.append((nc, steps+1))

for r, row in enumerate(heights):
    for c, col in enumerate(row):
        if col == 'S':
            print(find_shortest_path((r,c), heights))

# part 2

min_steps = float('inf')
for r, row in enumerate(heights):
    for c, col in enumerate(row):
        if col == 'S' or col == 'a':
            path = find_shortest_path((r,c), heights)
            if path:
                min_steps = min(min_steps, path)
print(min_steps)