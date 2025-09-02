'''
Is there a way to calculate checksum without expanding the input

- expand the disk format
  - split string into characters, switch off adding dots and file ids

- compact the disk
  - start and end pointers, swapping, and skipping free spaces/file blocks
    - find last non empty space, find first empty space, swap


- calculate checksum -> easy

'''

with open('input.txt') as f:
  diskmap = f.read()

expmap, on_file = "", True
for idx, num in enumerate(diskmap):
  file_char = str(idx // 2) if on_file else "."
  exp_format = ''.join([file_char] * int(num))
  expmap += exp_format
  on_file = not on_file

start, end = 0, len(expmap) - 1

while end > start:
  pass

