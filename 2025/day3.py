'''
joltage value is 1 through 9
maximum number of two digits, read left to right, in a string
  - largest {x} in [0:n-1], followed by largest number after [x+1:n]
BF: look for every combination left to right of numbers in the string -> O(n^2)

- iterate through in a loop; pointer for largest digit seen, pointer for second largest seen after largest.
- if cur_idx > second_largest, reset second largest. if cur_idx > largest, reset both
- only can reset second_largest on last integer
'''

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

joltage = 0
for line in lines:
    tens = 0
    ones = 0
    for battery in line[:-1]:
        bat_num = int(battery)
        if bat_num > tens:
            tens = bat_num
            ones = -1
        elif bat_num > ones:
            ones = bat_num
    ones = max(ones, int(line[len(line)-1]))
    joltage += tens*10 + ones
print(joltage)

'''
part 2:

- first digit {x} is gonna be largest digit in [:-11]
- second digit is gonna be the largest digit in [x+1:-10]

- track start and ending index that you are searching for the largest value in
- go through and find max and position of max, update start and end values
- while loop until length of res string is 12
'''

joltage2 = 0
for line in lines:
  res = ''
  start, end = 0, 11
  while len(res) < 12:
      max_digit = 0
      max_idx = 0
      segment = line[start:-end] if end > 0 else line[start:]
      for idx, b in enumerate(segment):
          bat = int(b)
          if bat > max_digit:
              max_digit = bat
              max_idx = idx+start
      res += str(max_digit)
      start = max_idx+1
      end -= 1
  joltage2 += int(res)
print(joltage2)


