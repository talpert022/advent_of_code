# import input data
with open('input.txt', 'r') as txt:
    input = txt.read().split('\n')

def parse_instruction(instruction):

    cord_idx = 0
    cord_str = ''
    x1 = y1 = x2 = y2 = ''

    for char in instruction:

        if char.isdigit():
            cord_str += char
        elif not char.isdigit() and prev_char.isdigit():
            if cord_idx == 0:
                x1 = cord_str
            elif cord_idx == 1:
                y1 = cord_str
            elif cord_idx == 2:
                x2 = cord_str
            elif cord_idx == 3:
                y2 = cord_str

            cord_str = ''
            cord_idx += 1

        prev_char = char

    y2 = cord_str
    return int(x1), int(y1), int(x2), int(y2)

# Standardizes coordinates so that the first coordinate is always the one with the lower x value
def standardize_cords(x1, y1, x2, y2):
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    return x1, y1, x2, y2

def find_bad_vents(input):

    # Create vent 2d array
    vents = [[0 for x in range(1000)] for y in range(1000)]

    # Iterate through each input line
    for instruction in input:
        # Split each input line into x1, y1, x2, y2
        x1, y1, x2, y2 = parse_instruction(instruction)
        
        # Check if the vent input is a horizontal or vertical line
        if x1 == x2 or y1 == y2:
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])
            # Modify the 2d array based on vent line
            for row in range(y1, y2+1):
                for col in range(x1, x2+1):
                    vents[row][col] += 1

        # Check if vent input is a diagonal line
        if (abs(x1 - x2) == abs(y1 - y2)):
            x1, y1, x2, y2 = standardize_cords(x1, y1, x2, y2)
            positive_slope = True if y2 > y1 else False
            if positive_slope:
                for num in range(abs(x1 - x2)+1):
                    vents[y1 + num][x1 + num] += 1
            else:
                for num in range(abs(x1 - x2)+1):
                    vents[y1 - num][x1 + num] += 1

    # Count number of 2 or greater vents
    bad_vents = 0
    for row in range(len(vents)):
        for col in range(len(vents[row])):
            if vents[row][col] >= 2:
                bad_vents += 1

    return bad_vents

print(find_bad_vents(input))
