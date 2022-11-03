# read problem input
with open('input.txt', 'r') as txt:
    input = txt.read()

def total_present_houses(moves):
    xPos, yPos = 0, 0
    presents = { (xPos, yPos) : 1 }
    for move in moves: 
        if move == '^':
            yPos += 1
        elif move == '>':
            xPos += 1
        elif move == 'v':
            yPos -= 1
        else:
            xPos -= 1
        
        presents[(xPos, yPos)] = presents.get((xPos, yPos), 0) + 1

    return len(presents)

def two_santa_total_present_houses(moves):
    xPos, yPos = 0, 0
    r_xPos, r_yPos = 0, 0
    presents = { (xPos, yPos) : 2 }

    for idx, move in enumerate(moves):
        if idx % 2 == 0:
            if move == '^':
                yPos += 1
            elif move == '>':
                xPos += 1
            elif move == 'v':
                yPos -= 1
            else:
                xPos -= 1

            presents[(xPos, yPos)] = presents.get((xPos, yPos), 0) + 1
        else:
            if move == '^':
                r_yPos += 1
            elif move == '>':
                r_xPos += 1
            elif move == 'v':
                r_yPos -= 1
            else:
                r_xPos -= 1

            presents[(r_xPos, r_yPos)] = presents.get((r_xPos, r_yPos), 0) + 1

    return len(presents)

print(two_santa_total_present_houses(input))