with open('input.txt') as txt:
    input = txt.read()
    displays = input.split('\n')

## PART 1
segments = []
for display in displays:
    display_segment = display.split(' ')
    output_segments = display_segment[-4:]
    segments += output_segments

unique_length_outputs = 0
for segment in segments:
    if len(segment) in [2,4,3,7]:
        unique_length_outputs += 1

# print(unique_length_outputs)

## PART 2

numbers = []
for display in displays:
    display_segment = display.split(' ')
    output_segments = display_segment[-4:]
    input_segments = display_segment[:10]
    numbers += [[input_segments, output_segments]]

number_wires = [
    [0,1,2,4,5,6], 
    [2,5], 
    [0,2,3,4,6], 
    [0,2,3,5,6], 
    [1,2,3,5], 
    [0,1,3,5,6], 
    [0,1,3,4,5,6], [0,2,5], 
    [0,1,2,3,4,5,6], 
    [0,1,2,3,5,6]
]

def find_display_mapping(input_segments):

    # Find 2nd and 5th wire combo with the one segment
    one_segment = [x for x in input_segments if len(x) == 2][0]
    second_fifth_wires = [one_segment[0], one_segment[1]]

    # Find 0th wire with one and seven numbers
    seven_segment = [x for x in input_segments if len(x) == 3][0]
    zero_wire = [char for char in seven_segment if char not in second_fifth_wires]

    # Find 1st and 3rd wire combo with four segment
    four_segment = [x for x in input_segments if len(x) == 4][0]
    first_third_wires = [char for char in four_segment if char not in second_fifth_wires]

    # Find 6th wire with nine segment
    almost_nine_wires = second_fifth_wires + first_third_wires + zero_wire
    nine_segment = [x for x in input_segments if set(almost_nine_wires).issubset(x) and len(x) == 6][0]
    sixth_wire = [char for char in nine_segment if char not in almost_nine_wires]

    # Find 2nd wire and 5th with five segment
    five_wires_one = zero_wire + sixth_wire + first_third_wires + [second_fifth_wires[0]]
    five_wires_two = zero_wire + sixth_wire + first_third_wires + [second_fifth_wires[1]]
    five_segment = [x for x in input_segments if set(x) == set(five_wires_one) or set(x) == set(five_wires_two)][0]
    second_wire = [char for char in second_fifth_wires if char not in five_segment]
    fifth_wire = [char for char in second_fifth_wires if char in five_segment]

    # Find 4th wire with six segment
    almost_six_wires = zero_wire + first_third_wires + fifth_wire + sixth_wire
    six_segment = [x for x in input_segments if set(almost_six_wires).issubset(x) and second_wire[0] not in x and len(x) == 6][0]
    fourth_wire = [char for char in six_segment if char not in almost_six_wires]

    # Find 1st and 3rd wires with two segment
    two_wires_one = zero_wire + second_wire + fourth_wire + sixth_wire + [first_third_wires[0]]
    two_wires_two = zero_wire + second_wire + fourth_wire + sixth_wire + [first_third_wires[1]]
    two_segment = [x for x in input_segments if set(x) == set(two_wires_one) or set(x) == set(two_wires_two)][0]
    first_wire = [char for char in first_third_wires if char not in two_segment]
    third_wire = [char for char in first_third_wires if char in two_segment]

    segment_mapping = { zero_wire[0]:0,
                        first_wire[0]:1,
                        second_wire[0]:2,
                        third_wire[0]:3,
                        fourth_wire[0]:4,
                        fifth_wire[0]:5,
                        sixth_wire[0]:6
    }

    return segment_mapping

total = 0
for input, output in numbers:
    wire_mapping = find_display_mapping(input)
    output_num = ''
    for num in output:
        display_wires = []
        for char in num:
            display_wires += [wire_mapping[char]]
        for idx, digit_wires in enumerate(number_wires):
            if set(digit_wires) == set(display_wires):
                output_num += str(idx)
    print(output_num)
    total += int(output_num) 

print(total)