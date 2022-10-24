import time

# read problem input
with open('input.txt', 'r') as txt:
    floors = txt.read()

# brute force
def part_one(floor_str):
    level = 0
    for instruction in floor_str:
        level += 1 if instruction == '(' else -1
    return level

def part_one_faster(floor_str):
    level = 0
    last = len(floor_str)
    for instruction in range(0, last//2):
        level += 1 if floor_str[instruction] == '(' else -1
        level += 1 if floor_str[last - 1 - instruction] == '(' else -1
    
    if len(floor_str) % 2 != 0:
        level += 1 if floor_str[last//2] == '(' else -1

    return level

def part_two(floor_str):
    level = 0
    for idx, instruction in enumerate(floor_str):
        level += 1 if instruction == '(' else -1
        if level < 0:
            return idx + 1
    return -1 

start = time.time()
final_level = part_two(floors)
end = time.time()
print(f'{(end - start) * 10**3} ms')
print(final_level)