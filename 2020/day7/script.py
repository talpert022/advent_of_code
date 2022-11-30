from collections import deque

with open('input.txt') as txt:
    input = txt.read().splitlines()

'''



'''
# part 1

# rule_set = {}
# for rule in input:
#     outer_rule, inner_rule = rule.split(' contain ')
#     inner_bags = [" ".join(bag.split()[1:3]) for bag in inner_rule.split(', ')]
#     outer_bag = " ".join(outer_rule.split()[:2])
#     rule_set[outer_bag] = inner_bags

# q = deque(['shiny gold'])
# vis = []
# outer_bag_count = 0
# while q:
#     inner_bag = q.popleft()
#     for out_bag, in_bags in rule_set.items():
#         if inner_bag in in_bags and out_bag not in vis:
#             outer_bag_count += 1
#             q.append(out_bag)
#             vis.append(out_bag)

# print(outer_bag_count)

# part 2

rule_set = {}
for rule in input:
    outer_rule, inner_rule = rule.split(' contain ')
    if inner_rule == 'no other bags.':
        inner_bags = []
    else:
        inner_bags = [(int(bag[0]), " ".join(bag.split()[1:3])) for bag in inner_rule.split(', ')]
    outer_bag = " ".join(outer_rule.split()[:2])
    rule_set[outer_bag] = inner_bags

contained_bags = 0
q = deque([(1, 'shiny gold')])
while q:
    mult, ob = q.popleft()
    for num, style in rule_set[ob]:
        contained_bags += mult*num
        q.append((mult*num, style))

print(contained_bags)