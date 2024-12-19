with open('input.txt') as txt:
    lines = txt.read().splitlines()

letters = [[char for char in line] for line in lines]

'''
Ideas:
(chosen) - Collect every horizontal, vertical, and diagonal segment of length 4 and check for "XMAS" or "SAMX" 
- Iterate through 2D array and when you encounter, X, use a subprocess to look for matches
'''

SEGMENT_LENGTH = 4
segments = []
for r,_ in enumerate(letters):
    for c,_ in enumerate(letters[r]):
        horizontally_fucked = c + SEGMENT_LENGTH > len(letters[r])
        vertically_fucked = r + SEGMENT_LENGTH > len(letters)

        if not horizontally_fucked: 
            segments += [[letters[r][c+i] for i in range(SEGMENT_LENGTH)]]
        if not vertically_fucked:
            segments += [[letters[r+i][c] for i in range(SEGMENT_LENGTH)]]
        if not horizontally_fucked and not vertically_fucked: # diagonal
            segments += [[letters[r+i][c+i] for i in range(SEGMENT_LENGTH)]]
        if c >= SEGMENT_LENGTH-1 and not vertically_fucked: # reverse diagonal
            segments += [[letters[r+i][c-i] for i in range(SEGMENT_LENGTH)]]

count = len([seg for seg in segments if ''.join(seg) in ["XMAS", "SAMX"]])
print(count)

# PART 2

crossed_mas = 0
for r in range(1, len(letters)-1):
    for c in range(1, len(letters[r])-1):
        if letters[r][c] != 'A':
            continue

        if {letters[r-1][c-1], letters[r+1][c+1]} != {'M', 'S'}:
            continue

        if {letters[r+1][c-1], letters[r-1][c+1]} != {'M', 'S'}:
            continue
        
        crossed_mas += 1

print(crossed_mas)