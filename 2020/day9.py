with open('input.txt') as txt:
    digits = list(map(int, txt.read().splitlines()))

# part1: 13:24
start = 0
for num in digits[25:]:
    preamble = digits[start:start+25]
    allowed = False
    for idx, first in enumerate(preamble):
        target = num - first
        if target in preamble and preamble.index(target) != idx:
            allowed = True
            break
    if not allowed:
        invalidNum = num
        print(invalidNum)
    start += 1

# part2: 9:39
s = 0
e = 0
while e <= len(digits):
    contiguous_set = digits[s:e]
    sumset = sum(contiguous_set)
    if sumset < invalidNum:
        e += 1
    elif sumset > invalidNum:
        s += 1
    else:
        sortset = sorted(contiguous_set)
        print(sortset[0] + sortset[-1])
        break