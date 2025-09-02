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

while end > start:
  if expmap[start] == -1 and expmap[end] != -1:
    expmap[start], expmap[end] = expmap[end], expmap[start]

  start += 1 if expmap[start] != -1 else 0
  end -= 1 if expmap[end] == -1 else 0

print(expmap[:50])
checksum = 0
for idx, file_val in enumerate(expmap):
  if file_val == -1: break
  checksum += int(file_val)*idx

print(checksum)