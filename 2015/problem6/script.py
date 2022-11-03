# read problem input
with open('input.txt', 'r') as txt:
    input = txt.read()
    instructions = input.splitlines()

def instruction_parser(instruction):
    spaces = 0
    command = ''
    start_x = ''
    start_y = ''
    end_x = ''
    end_y = ''
    idx = 0

    while idx < len(instruction):
        char = instruction[idx]
        if command == 'toggle' and spaces == 0:
            spaces += 1

        if char == ' ':
            spaces += 1
        elif char == ',':
            spaces += 1
        else:
            if 0 <= spaces <= 1:
                command += char
            elif spaces == 2:
                start_x += char
            elif spaces == 3:
                start_y += char
            elif spaces == 5:
                end_x += char
            elif spaces == 6:
                end_y += char
        idx += 1

    return command, int(start_x), int(start_y), int(end_x), int(end_y)

def total_on_lights(instructions):
    lights = [[0 for row in range(0,1000)] for col in range(0,1000)]
    parsing_error = Exception('Error parsing instruction')
    
    for itr in instructions:
        try:
            command, start_x, start_y, end_x, end_y = instruction_parser(itr)
        except:
            raise parsing_error

        if command == 'turnon':
            for row in range(start_x, end_x):
                for col in range(start_y, end_y):
                    lights[row][col] = 1
        elif command == 'turnoff':
            for row in range(start_x, end_x):
                for col in range(start_y, end_y):
                    lights[row][col] = 0
        elif command == 'toggle':
            for row in range(start_x, end_x):
                for col in range(start_y, end_y):
                    lights[row][col] = 1 if lights[row][col] == 0 else 0
        else:
            raise parsing_error

    total_on = 0
    for row in range(len(lights)):
        for col in range(len(lights[row])):
            total_on += lights[row][col]

    return total_on
    pass
    


print(instruction_parser('toggle 756,965 through 812,992'))
print(instructions)
print(total_on_lights(instructions))
