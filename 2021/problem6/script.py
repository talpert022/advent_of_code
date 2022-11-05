# import input data
with open('input.txt') as txt:
    input = txt.read()
    fishes = [int(day_count) for day_count in input.split(',')]

# create age -> fish count dict from fish array
age_count = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
for fish in fishes:
    age_count[fish] += 1

def num_fish_after(fish, days):
    oldest_age = len(fish)-1
    age_groups = list(reversed(fish.keys()))[1:]
    # iterate over the number of days, exclusive of the last day
    for _ in range(days):
        # iterate over keys in fish dictionary, reverse from seven to zero
        last_group_count = fish[oldest_age]
        for group in age_groups:
            # switch age key with the age + 1 key, and store that key in a temp
            fish[group], last_group_count = last_group_count, fish[group]
        # special case for zero key
        fish[6] += last_group_count
        fish[8] = last_group_count

    # return sum of counts in fish dictionary
    return sum(fish.values())

PT1_DAYS = 80
PT2_DAYS = 256

print(num_fish_after(age_count, PT1_DAYS))