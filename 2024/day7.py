import re

with open('input.txt') as txt:
  lines = txt.read().splitlines()

equations = []
for line in lines:
  value, numbers = line.split(':')
  num_list = [int(num) for num in re.findall(r'(\d+)+', numbers)]
  equations.append((int(value),num_list))

r = 0
for value,numbers in equations:
  results = [numbers[0]]
  for num in numbers[1:]:
    new_results = []
    for res in results:
      new_results.append(res+num)
      new_results.append(res*num)
      new_results.append(int(str(res)+str(num))) # comment out for part 1
    results = new_results
  r += value if value in results else 0

print(r)