import time

start1 = time.perf_counter()

with open('input.txt', 'r') as f:
  lines = f.read().splitlines()

grid = [[0 if space != "." else space for space in line] for line in lines]
adjacent = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

n,m = len(grid), len(grid[0])
for i in range(n):
  for j in range(m):
    if grid[i][j] != ".":
      for x,y in adjacent:
        if 0 <= i+x < n and 0 <= j+y < m and grid[i+x][j+y] != ".":
          grid[i+x][j+y] += 1

res = 0
for i in range(n):
  for j in range(m):
    if grid[i][j] != "." and grid[i][j] < 4:
      res += 1

print(res)

# part 2

res2 = 0
made_removal = True
while made_removal:
  made_removal = False
  for i in range(n):
    for j in range(m):
      if grid[i][j] != "." and grid[i][j] < 4:
        made_removal = True
        res2 += 1
        grid[i][j] = "."
        for x,y in adjacent:
          if 0 <= i+x < n and 0 <= j+y < m and grid[i+x][j+y] != ".":
            grid[i+x][j+y] -= 1

print(res2)

end1 = time.perf_counter()

start2 = time.perf_counter()

from collections import deque
def solve(text):
    lines = text.strip().splitlines()
    rows, cols = len(lines), len(lines[0])
    W = cols + 2  # padded width to avoid bounds checks
    H = rows + 2

    # Flat padded grid: 1 = roll, 0 = empty (padding is all 0)
    grid = bytearray(W * H)
    for r, line in enumerate(lines):
        base = (r + 1) * W + 1
        for c, ch in enumerate(line):
            if ch == '@':
                grid[base + c] = 1

    offsets = (-W - 1, -W, -W + 1, -1, 1, W - 1, W, W + 1)

    # Initial neighbor counts for every roll
    counts = bytearray(W * H)
    rolls = [i for i in range(W, W * (H - 1)) if grid[i]]
    for i in rolls:
        counts[i] = sum(grid[i + d] for d in offsets)

    # Part 1: rolls with fewer than 4 neighbors
    initial = [i for i in rolls if counts[i] < 4]
    part1 = len(initial)

    # Part 2: cascade removal. Neighbor counts only ever decrease, so once a
    # roll becomes accessible it stays accessible — batch order doesn't matter
    # and a single BFS pass gives the exact answer in O(cells) total work.
    queue = deque(initial)
    for i in initial:
        grid[i] = 0
    part2 = 0
    while queue:
        i = queue.popleft()
        part2 += 1
        for d in offsets:
            j = i + d
            if grid[j]:
                counts[j] -= 1
                if counts[j] == 3:  # just dropped below 4
                    grid[j] = 0
                    queue.append(j)
    return part1, part2

with open("input.txt") as f:
    p1, p2 = solve(f.read())

print("Part 1:", p1)
print("Part 2:", p2)

end2 = time.perf_counter()

print(end1-start1)
print(end2-start2)