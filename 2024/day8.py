'''
isolate positions (r,c) of all antenna pairings of the same type
- every antenna has a pairing with every other antenna of the same type. 
- need to dedup pairings with the same antenna positions
- Iterating through spaces, create dict of letter to positions mappings, then create array of pairings by iterating forward through mappings

some calculation of the slope between first and second antenna, that can be applied to them to get antinode positions
- from whichever node is point A, find delta x,y to point B, apply those values to positivly to point B and negatively to point A

Im assuming antinodes can't overlap each other
'''

with open('input.txt') as txt:
  grid = [list(row) for row in txt.read().splitlines()]

antennas = dict()
for n in range(len(grid)):
  for m in range(len(grid[0])):
    space = grid[n][m]
    if space == '.':
      continue
    antennas[space] = antennas.get(space, []) + [(n,m)]

pairings = list()
for k,values in antennas.items():
  for idx,pointA in enumerate(values):
    for pointB in values[idx+1:]:
      pairings.append([pointA, pointB])

res = set()
for pointA, pointB in pairings:
  slope = pointB[0] - pointA[0], pointB[1] - pointA[1]
  antinodes = (pointB[0] + slope[0], pointB[1] + slope[1]), (pointA[0] - slope[0], pointA[1] - slope[1])
  for r,c in antinodes:
    if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
      res.add((r,c))

# Part 2
'''
- to get expanded list of antinodes, multiply slope by increasing integers, adding and subtracting from og antennas
- when both antinodes are out of bounds, don't need to calculate more points
'''

res_two = set()
for pointA, pointB in pairings:
  slope = pointB[0] - pointA[0], pointB[1] - pointA[1]
  for multiplier in range(20):
    delta_x, delta_y = slope[0]*multiplier, slope[1]*multiplier
    antinodes = (pointB[0] + delta_x, pointB[1] + delta_y), (pointA[0] - delta_x, pointA[1] - delta_y)
    
    node_added = False
    for r,c in antinodes:
      if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
        grid[r][c] = "#"
        res_two.add((r,c))
        node_added = True
    
    if not node_added:
      break

print(grid)
print(len(res_two))
