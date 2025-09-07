from copy import deepcopy
'''
Is there a way to calculate checksum without expanding the input

- expand the disk format
  - split string into characters, switch off adding dots and file ids

- compact the disk
  - start and end pointers, swapping, and skipping free spaces/file blocks
    - find first empty space, find last non empty space, swap

- calculate checksum -> easy

'''

with open('input.txt') as f:
  diskmap = f.read()

expmap, on_file = [], True
for idx, num in enumerate(diskmap):
  file_id = idx // 2 if on_file else -1
  expmap.extend([file_id] * int(num))
  on_file = not on_file

start, end = 0, len(expmap) - 1
expmap2 = deepcopy(expmap)

while end > start:
  if expmap[start] == -1 and expmap[end] != -1:
    expmap[start], expmap[end] = expmap[end], expmap[start]

  start += 1 if expmap[start] != -1 else 0
  end -= 1 if expmap[end] == -1 else 0

checksum = 0
for idx, file_val in enumerate(expmap):
  if file_val == -1: break
  checksum += int(file_val)*idx

print(checksum)

'''
Part 2
- compile list of free space (ranges of starting to stop position) in the disk
- iterate backwards through file Ids and get full range of contiguous positions (as a range)
- compare left -> right w free space positions, once found match, adjust the expmap with a group swap and free space array

HAS TO BE TO THE LEFT: don't need to add in free space from swapped positions

'''

def get_freespaces(diskmap):
  res, is_free, span = [], False, [0,0]
  for idx, space in enumerate(diskmap):
    if space == -1 and not is_free:
      is_free = True
      span[0] = idx
    elif is_free and space != -1:
      span[1] = idx-1
      res.append([span[0], span[1]])
      is_free = False
  return res

freespaces = get_freespaces(expmap2)
filespan = [0,0]
idx = len(expmap2)-1
curr_file, in_file = 0, False
while idx >= 0:
  if expmap2[idx] != -1 and not in_file:
    filespan[0] = idx
    curr_file = expmap2[idx]
    in_file = True
  elif in_file and expmap2[idx] != curr_file:
    filespan[1] = idx+1
    in_file = False
    file_len = filespan[0] - filespan[1]
    # find leftmost length of free spaces less than or equal to filespan length, check up until second pos of filespan (strictly left)
    for space in freespaces:
      start,end = space
      if end < filespan[1] and end - start >= file_len:
        for i in range(file_len+1):
          expmap2[start+i], expmap2[filespan[1]+i] = expmap2[filespan[1]+i], expmap2[start+i]
        space[0] = space[0] + file_len + 1
        break
  else:
    idx -= 1

checksum2 = 0
for idx, file_val in enumerate(expmap2):
  if file_val == -1: continue
  checksum2 += int(file_val)*idx

print(checksum2)