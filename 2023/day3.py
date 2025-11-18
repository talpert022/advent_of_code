with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

'''
- isolate numbers in the engine
    - iterate through 2d array, skip periods, 
    - append numbers to list when they are in a row. when period interrupts, create int

- for each digit in a number, get list of adjacent positions
    - if adjacent position is (period, number, **symbol**), add number to sum

- how to check for symbol
    - BF: recheck for each digit all the surrounding 8 positions
    - compile a list of adjacent positions that ignore duplicates as you create the number
    - store position values in lookup dict to NOT recheck positions
'''

def issymbol(char):
    return not char.isdigit() and char != "."

def add_adj_positions(adj_set: set, r, c, n, m):
    directions = [[-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1]]
    for dr, dc in directions:
        x,y = r+dr, c+dc
        if 0 <= x < n and 0 <= y < m:
            adj_set.add((x,y))

res = 0
n,m = len(lines), len(lines[0])
for r in range(n):
    in_num, num_list = False, ""
    adj_pos = set()
    for c in range(m):
        pos: str = lines[r][c]
        if pos.isdigit():
            in_num = True
            num_list += pos
            add_adj_positions(adj_pos, r, c, n, m)

        if (not pos.isdigit() or c == m-1) and in_num:
            print(adj_pos)
            is_adj_to_symbol = any(issymbol(lines[x][y]) for x,y in adj_pos)
            if is_adj_to_symbol:
                res += int(num_list)
            in_num, num_list, adj_pos = False, "", set()
            
print(res)