with open('input.txt') as txt:
    moves = txt.read().splitlines()

dir_offset = {'U': [0,1], 'D': [0,-1], 'L': [-1,0], 'R': [1,0]}
diff_correction = { (0,2):(0,1), (0,-2):(0,-1), (2,0):(1,0),(-2,0):(-1,0), \
    (-1,-2):(-1,-1), (-2,-1):(-1,-1), (1,-2):(1,-1), (2,-1):(1,-1), \
    (1,2):(1,1), (2,1):(1,1), (-2,1):(-1,1), (-1,2):(-1,1), 
    (2,2):(1,1), (-2,2):(-1,1), (-2,-2):(-1,-1), (2,-2):(1,-1) }

# hpos = [0,0]
# tpos = [0,0]
# unique_pos = {(0,0)}

# for move in moves:
#     dir, l = move.split()
#     for i in range(int(l)):
#         # move the head
#         hpos[0] += dir_offset[dir][0]
#         hpos[1] += dir_offset[dir][1]
#         # move tail in response
#         ht_diff = (hpos[0]-tpos[0], hpos[1]-tpos[1])
#         tpos[0] += diff_correction[ht_diff][0] if ht_diff in diff_correction else 0
#         tpos[1] += diff_correction[ht_diff][1] if ht_diff in diff_correction else 0
#         # add tail to position set
#         unique_pos.add((tpos[0], tpos[1]))

# print(len(unique_pos))

# part 2

hpos = [0,0]
tpos = [[0,0] for _ in range(9)]
unique_pos = {(0,0)}

for move in moves:
    dir, l = move.split()
    for i in range(int(l)):
        # move the head
        hpos[0] += dir_offset[dir][0]
        hpos[1] += dir_offset[dir][1]
        # move each tail knot in response
        last_knot = hpos
        for i, knot in enumerate(tpos):
            ht_diff = (last_knot[0]-knot[0], last_knot[1]-knot[1])
            knot[0] += diff_correction[ht_diff][0] if ht_diff in diff_correction else 0
            knot[1] += diff_correction[ht_diff][1] if ht_diff in diff_correction else 0
            last_knot = knot
        # add tail to position set
        unique_pos.add((tpos[8][0], tpos[8][1]))

print(len(unique_pos))

