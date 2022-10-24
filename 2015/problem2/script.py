import time

# read problem input
with open('input.txt', 'r') as txt:
    input = txt.read()
    inputArr = [[int(dimension) for dimension in line.split('x')] for line in input.split()]

def find_total_wrapping(inputArr):
    total_paper = 0
    for present in inputArr:
        sorted_dimensions = sorted(present)
        side1, side2, side3 = sorted_dimensions

        present_paper = 2*side1*side2 + 2*side1*side3 + 2*side2*side3
        present_paper += side1*side2
        total_paper += present_paper
    print(total_paper)

def find_total_ribbon(inputArr):
    total_ribbon = 0
    for present in inputArr:
        side1, side2, side3 = sorted(present)
        wrap_ribbon = side1*2 + side2*2
        bow_ribbon = side1*side2*side3
        total_ribbon += wrap_ribbon + bow_ribbon
    print(total_ribbon)

find_total_ribbon(inputArr)