with open('input.txt') as txt:
    input = txt.read().split('\n\n')
    groups = [group.split('\n') for group in input]

# part 1

# count = 0
# for group in groups:
#     yes_qs = set()
#     for person in group:
#         for question in person:
#             yes_qs.add(question)
#     count += len(yes_qs)

# print(count)

# part 2

count = 0
for group in groups:
    group_yes_qs = []
    for person in group:
        person_yes_qs = set()
        for question in person:
            person_yes_qs.add(question)
        group_yes_qs.append(person_yes_qs)
    
    count += len(set.intersection(*group_yes_qs))

print(count)
