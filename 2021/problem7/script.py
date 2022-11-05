with open('input.txt') as txt:
    input = txt.read()
    crabs = [int(day_count) for day_count in input.split(',')]

maxPos = max(crabs)
minPos = min(crabs)

## part 1
min_feul, min_feul_pos = float('inf'), -1
for pos in range(minPos, maxPos + 1):
    total_feul = 0
    for crab_pos in crabs:
        crab_feul = abs(pos - crab_pos)
        total_feul += crab_feul
    if total_feul < min_feul:
        min_feul, min_feul_pos = total_feul, pos

## part 2
min_feul, min_feul_pos = float('inf'), -1
for pos in range(minPos, maxPos + 1):
    total_feul = 0
    for crab_pos in crabs:
        crab_pos_diff = abs(pos - crab_pos)
        crab_feul = ((crab_pos_diff**2) + crab_pos_diff) // 2
        total_feul += crab_feul
    if total_feul < min_feul:
        min_feul, min_feul_pos = total_feul, pos

print(min_feul, min_feul_pos)