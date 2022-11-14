# import input data
with open('input.txt') as txt:
    seats = txt.read().splitlines()

# part 1

# top_id = -1
# for seat in seats:
#     row = seat[:7].replace('F', '0').replace('B', '1')
#     col = seat[-3:].replace('L', '0').replace('R', '1')
#     top_id = max(top_id, (int(row, 2) * 8) + int(col, 2))

# part 2

all_seats = []
for seat in seats:
    row = seat[:7].replace('F', '0').replace('B', '1')
    col = seat[-3:].replace('L', '0').replace('R', '1')
    all_seats += [(int(row, 2) * 8) + int(col, 2)]

sorted_seats = sorted(all_seats)
last_seat = sorted_seats[0]
for seat in sorted_seats[1:]:
    if seat == last_seat + 2:
        print(seat-1)
    last_seat = seat