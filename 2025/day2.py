from copy import copy
import re

pattern = re.compile(r"(\d+)-(\d+)")
with open('input.txt', 'r') as f:
    range_line = f.read()
    ranges = re.findall(pattern, range_line)

valid_seq_lens = { 1:[], 2:[1], 3:[1], 4:[1,2], 5:[1], 6:[1,2,3], 7:[1], 8:[1,2,4], 9:[1,3], 10:[1,2,5] }
def is_invalid(num_str):
  seq_lens = copy(valid_seq_lens[len(num_str)])
  for idx, c in enumerate(num_str):
      lens_to_remove = []
      for length in seq_lens:
          if c != num_str[idx % length]:
              lens_to_remove.append(length)
      for length in lens_to_remove: seq_lens.remove(length)
  return True if len(seq_lens) else False

res = 0
res2 = 0
for id_range in ranges:
    start,end = int(id_range[0]), int(id_range[1])
    for x in range(start, end+1):
        id = str(x)
        first,second = id[:len(id)//2], id[len(id)//2:]
        if first == second:
            res += x
        if is_invalid(id):
            res2 += x
print(res)
print(res2)


