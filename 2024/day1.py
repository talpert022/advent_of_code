# Must be in first 50 places == 50 stars
# array sort, absolute value

import re

# PART 1

with open('input.txt') as txt:
    lines = txt.read().splitlines()

pattern = re.compile(r'(\d+)\s+(\d+)')

left_locations = [int(cords[0]) for cords in [re.findall(pattern, line)[0] for line in lines]]
right_locations = [int(cords[1]) for cords in [re.findall(pattern, line)[0] for line in lines]]

left_locations.sort()
right_locations.sort()

total_distance = 0
for idx in range(len(left_locations)):
    total_distance += abs(left_locations[idx] - right_locations[idx])

print(total_distance)

# PART 2

right_freqs = {}
for cord in right_locations:
    right_freqs.setdefault(cord, 0)
    right_freqs[cord] += 1

similarity_score = 0
for cord in left_locations:
    similarity_score += cord * right_freqs.get(cord, 0)

print(similarity_score)
