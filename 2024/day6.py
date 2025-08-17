'''
carrot indicated direction in 2d array

If there is something directly in front of you, turn right 90 degrees.
Otherwise, take a step forward.

Include start position of guard in total spaces
--------------

(create 2d array from input at get position of carrot (or different directional arrow))

while loop on the conditional that next_x and next_y are not out of bounds
- check new space, implicit OOB check in while loop
manipulate x,y depending on var direction (0-3), 
        r,c = next_r, next_c if ".", count space
        don't change r,c; next_r, next_c = direction + r,c; if you hit "#", change direction, don't count space

how to count spaces? -- set of (x,y)
- previously hit spaces 

'''

with open('input.txt') as txt:
  lines = txt.read().splitlines()

grid_arr = [[char for char in line] for line in lines]

r,c = None, None
for idx, row in enumerate(grid_arr):
  if '^' in row:
    r,c = idx, row.index('^')

unique_spaces = {(r,c)}
direction = [(-1,0), (0,1), (1,0), (0,-1)]
guard_dir = 0

next_r, next_c = r + direction[guard_dir][0], c + direction[guard_dir][1]

while 0 <= next_r < len(grid_arr) and 0 <= next_c < len(grid_arr[0]):
  next_space = grid_arr[next_r][next_c]
  if next_space == "#":
    guard_dir = (guard_dir + 1) % 4
  else:
    r,c = next_r, next_c
    unique_spaces.add((r,c))

  next_r, next_c = r + direction[guard_dir][0], c + direction[guard_dir][1]
  
print(len(unique_spaces))