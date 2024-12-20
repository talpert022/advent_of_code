with open('input.txt') as txt:
    lines = txt.read().splitlines()

section_split_idx = lines.index('')
rules_lines = lines[:section_split_idx]
updates_lines = lines[section_split_idx+1:]

# data processing for part 1
rules = [[int(page) for page in line.split('|')] for line in rules_lines]
collated_rules = {} # IIRC js's chosen word for combine lol
for rule in rules:
    if rule[0] in collated_rules:
        collated_rules[rule[0]].add(rule[1])
    else:
        collated_rules[rule[0]] = set([rule[1]])
updates = [[int(page) for page in line.split(',')] for line in updates_lines]

'''
PART 1
'''

def is_right_order(update):
    for idx, page in enumerate(update[:-1]):
        pages_after = update[idx+1:]
        if page not in collated_rules: return False
        if not set(pages_after).issubset(collated_rules[page]): return False
    return True

sum = 0
for update in updates:
    if is_right_order(update):
        sum += update[len(update)//2]

print(sum)

'''
PART 2
'''
