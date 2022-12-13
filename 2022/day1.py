with open('input.txt') as txt:
    input = txt.read()
    elves = input.split('\n\n')

# part 1

topelf = float('-inf')
for elf in elves:
    cals = [int(cal) for cal in elf.splitlines()]
    topelf = max(topelf, sum(cals))

# improvment

topelf = max([sum(list(map(int, line.split()))) for line in elves])

print(topelf)

# part 2

elf_cals = [sum([int(cal) for cal in elf.splitlines()]) for elf in elves]
print(sum(sorted(elf_cals, reverse=True)[:3]))