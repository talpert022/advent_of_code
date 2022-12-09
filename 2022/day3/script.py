from webbrowser import get


with open('input.txt') as txt:
    input = txt.read().splitlines()

splits = []
for rucksack in input:
    n = len(rucksack)
    splits.append([rucksack[:n//2], rucksack[n//2:]])

def get_priority(char):
    if char.isupper():
        return ord(char) - 64 + 26
    else:
        return ord(char) - 96

r = 0
for start, end in splits:
    for c in start:
        if c in end:
            r += get_priority(c)
            break

print(r)

# part 2

threesplit = []
group = []
for idx, rucksack in enumerate(input):
    group.append(set(rucksack))
    if idx % 3 == 2:
        threesplit.append(group)
        group = []

r = 0
for a,b,c in threesplit:
    badge = a.intersection(b, c)
    r += get_priority(list(badge)[0])

print(r)