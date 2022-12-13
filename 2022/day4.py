import re

with open('input.txt') as txt:
    input = txt.read().splitlines()
    

sections = [re.findall(r'(\d+)-(\d+),(\d+)-(\d+)', line)[0] for line in input]

# part 1

# overlapping = 0
# for a1,b1,c1,d1 in sections:
#     a,b,c,d = list(map(int,[a1,b1,c1,d1]))
#     if (a >= c and b <= d) or (c >= a and d <= b):
#         overlapping += 1

# print(overlapping)

# part 2

overlapping = 0
for a1,b1,c1,d1 in sections:
    a,b,c,d = list(map(int,[a1,b1,c1,d1]))
    if not (b < c or d < a):
        overlapping += 1

print(overlapping)