with open('input.txt') as txt:
    signals = txt.read().split('\n\n')

def extract(list):
    items = []
    inlist = 0
    item = ''
    for c in list:
        if c == ',' and inlist == 0:
            items.append(item)
            item = ''
        else:
            item += c
            if c == '[':
                inlist += 1
            elif c == ']':
                inlist -= 1
    if item:
        items.append(item)
    return items

def compare(left, right):
    l = 0
    r = 0
    print(left, right)
    while l < len(left) and r < len(right):
        if left[l][0] == '[':
            left_items = extract(left[l][1:-1])
            if right[r][0] == '[':
                right_items = extract(right[r][1:-1])
            else:
                right_items = right[r]
            c = compare(left_items, right_items)
        elif right[r][0] == '[':
            right_items = extract(right[r][1:-1])
            c = compare(left[l], right_items)
        else:
            num1 = int(left[l])
            num2 = int(right[r])
            if num1 < num2:
                c = 1
            elif num2 < num1:
                c = 2
            else:
                c = 0

        if c != 0:
            return c
        else:
            if l == len(left) - 1 and r < len(right) - 1:
                return 1
            elif r == len(right) - 1 and l < len(left) - 1:
                return 2
        
        l += 1
        r += 1

    if len(left) == 0 and len(right) > 0:
        return 1
    elif len(right) == 0 and len(left) > 0:
        return 2
    else:
        return 0

inorder = 0
for idx, pair in enumerate(signals):
    left, right = pair.splitlines()
    if compare([left], [right]) in [0,1]:
        print(f'inorder: {idx + 1}')
        inorder += idx + 1

print(inorder)