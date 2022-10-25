# read problem input
with open('input.txt', 'r') as txt:
    input = txt.read()
    inputArr = input.split()

def is_nice(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    double_letter = False
    for idx, char in enumerate(str):
        if idx >= 1:
            lastTwo = str[idx-1:idx+1]
            if lastTwo == 'ab' or lastTwo == 'cd' or lastTwo == 'pq' or lastTwo == 'xy':
                return False
            if char == str[idx-1]:
                double_letter = True
        if char in vowels:
            vowel_count += 1
    return vowel_count >= 3 and double_letter

def is_nice_two(str):
    interrupted_repeat = False
    has_non_overlapping_pair = False

    for idx, char in enumerate(str):
        if idx >= 1:
            pair = str[idx-1:idx+1]
            if pair in str[idx+1:]:
                has_non_overlapping_pair = True
        if idx >= 2:
            if char == str[idx-2]:
                interrupted_repeat = True

    return has_non_overlapping_pair and interrupted_repeat


def num_nice_strs(words):
    num_nice = 0
    for word in words:
        num_nice += 1 if is_nice(word) else 0
    return num_nice

print(num_nice_strs(inputArr))