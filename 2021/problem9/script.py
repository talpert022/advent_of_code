# import input data
from functools import reduce

with open('input.txt') as txt:
    input = txt.read().split('\n')
    cave_heights = [[int(height) for height in row] for row in input]

## part 1

# risk = 0
# for i in range(len(cave_heights)):
#     for j in range(len(cave_heights[i])):
#         elevation = cave_heights[i][j]
#         low_left = j == 0 or (j > 0 and cave_heights[i][j-1] > elevation)
#         low_right = j == len(cave_heights[i]) - 1 or (j < len(cave_heights[i]) - 1 and cave_heights[i][j+1] > elevation)
#         low_up = i == 0 or (i > 0 and cave_heights[i-1][j] > elevation)
#         low_down = i == len(cave_heights) - 1 or (i < len(cave_heights) - 1 and cave_heights[i+1][j] > elevation)
#         low_point = low_left and low_right and low_up and low_down

#         if low_point:
#             print(f'row: {i}, col: {j}, level: {elevation}')
#             risk += elevation + 1

# print(risk)

## part 2

def find_basin_size(i, j, heights):

    # add current point to start of operation queue
    queue = [[i, j]]
    visited = [[i, j]]
    basin_size = 0

    while queue:

        # increment basin_size for each traversed height
        row, col = queue.pop(0)
        basin_size += 1

        elevation = heights[row][col]
        # determine bools for valid basins
        if col > 0 and elevation < heights[row][col-1] < 9 and [row, col-1] not in visited:
            queue += [[row, col-1]]
            visited += [[row, col-1]]
        if row < len(heights) - 1 and elevation < heights[row+1][col] < 9 and [row+1, col] not in visited:
            queue += [[row+1, col]]
            visited += [[row+1, col]]
        if col < len(heights[0]) - 1 and elevation < heights[row][col+1] < 9 and [row, col+1] not in visited:
            queue += [[row, col+1]]
            visited += [[row, col+1]]
        if row > 0 and elevation < heights[row-1][col] < 9 and [row-1, col] not in visited:
            queue += [[row-1, col]]
            visited += [[row-1, col]]
    
    return basin_size
    
basins = []
for i in range(len(cave_heights)):
    for j in range(len(cave_heights[i])):
        elevation = cave_heights[i][j]
        basin_size = find_basin_size(i, j, cave_heights)
        print(f'row: {i}, col: {j}, level: {elevation}, basin: {basin_size}')
        basins += [basin_size]

print(sorted(basins, reverse=True)[:3])
print(reduce(lambda x,y: x * y , sorted(basins, reverse=True)[:3]))