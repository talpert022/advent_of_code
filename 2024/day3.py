import re

# PART 1

with open('input.txt') as txt:
    corrupted_memory = txt.read()

pattern = re.compile(r'mul\(\d+\,\d+\)')
valid_matches = re.findall(pattern, corrupted_memory)

sum = 0
for match in valid_matches:
    x,y = re.findall(r'\d+', match)
    sum += int(x) * int(y)

print(sum)

# PART 2

pattern = re.compile(r'mul\(\d+\,\d+\)|do\(\)|don\'t\(\)')
valid_matches = re.findall(pattern, corrupted_memory)

sum = 0
enabled = 1
for match in valid_matches:
    if not match.startswith("mul"):
        enabled = 0 if match == "don't()" else 1
        continue

    if not enabled:
        continue

    x,y = re.findall(r'\d+', match)
    sum += int(x) * int(y)

print(sum)