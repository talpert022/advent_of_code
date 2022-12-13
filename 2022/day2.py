with open('input.txt') as txt:
    input = txt.read().splitlines()
    rounds = [round.split(' ') for round in input]

def round_score(op, rps):
    score = 0
    # game outcome score
    if (op == 'A'):
        if (rps == 'Y'):
            score += 6
        elif (rps == 'X'):
            score += 3
    elif (op == 'B'):
        if (rps == 'Y'):
            score += 3
        elif (rps == 'Z'):
            score += 6
    else:
        if (rps == 'X'):
            score += 6
        elif (rps == 'Z'):
            score += 3
    # your hand score

    if (rps == 'X'):
        score += 1
    elif (rps == 'Y'):
        score += 2
    else:
        score += 3

    return score

tot_score = 0
for op, rps in rounds:
    tot_score += round_score(op, rps)

print(tot_score)

# part 2

def find_play(op, outcome):
    if (op == 'A'):
        if (outcome == 'X'):
            return 'Z'
        elif (outcome == 'Y'):
            return 'X'
        else:
            return 'Y'
    elif (op == 'B'):
        if (outcome == 'X'):
            return 'X'
        elif (outcome == 'Y'):
            return 'Y'
        else:
            return 'Z'
    else:
        if (outcome == 'X'):
            return 'Y'
        elif (outcome == 'Y'):
            return 'Z'
        else:
            return 'X'

tot_score_again = 0
for op, rps in rounds:
    new_rps = find_play(op, rps)
    tot_score_again += round_score(op, new_rps)

print(tot_score_again)