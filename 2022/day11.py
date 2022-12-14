from functools import reduce
import re

with open('input.txt') as txt:
    monkeys = txt.read().split('\n\n')

items = [[] for monkey in monkeys]
worryops = [[] for monkey in monkeys]
tests = [[] for monkey in monkeys]
for idx, monkey in enumerate(monkeys):
    # parse monkey item 
    lines = monkey.splitlines()
    m_items = [int(item) for item in re.findall(r'\b(\d+),*\b', lines[1])]
    items[idx] += m_items
    # parse worry operation
    op = re.search(r'[\+\*]', lines[2]).group()
    term = re.search(r'\w+$', lines[2]).group()
    worryops[idx] += [op, term]
    # parse test function
    testnums = [int(num) for num in re.findall(r'\d+$', '\n'.join(lines[3:6]), flags=re.MULTILINE)]
    tests[idx] += testnums

inspections = [0 for monkey in monkeys]
ROUNDS = 10000 # change to 20 for part 1
for i in range(ROUNDS):
    for x, monkey_items in enumerate(items):
        while monkey_items:
            worry = monkey_items[0]
            inspections[x] += 1
            items[x].remove(worry)

            # perform worry operation on item
            op, term = worryops[x]
            if op == '*':
                worry *= int(term) if term.isdigit() else worry
            else:
                worry += int(term) if term.isdigit() else worry

            worry %= reduce(lambda x,y: x*y, [t[0] for t in tests]) # change modulo to 3 for part 1

            # perform test to throw item
            div, t, f = tests[x]
            if worry % div == 0:
                items[t].append(worry)
            else:
                items[f].append(worry)

print(inspections)
print(reduce(lambda x,y: x*y, sorted(inspections, reverse=True)[:2]))