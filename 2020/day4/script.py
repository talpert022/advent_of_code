with open('input.txt') as txt:
    input = txt.read().splitlines()

# part 1

# passports = []
# p = ''
# for idx, line in enumerate(input):
#     if line == '':
#         fields = p.split(' ')[:-1] # discarding extra space at the end
#         passports += [[field[:3] for field in fields]]
#         p = ''
#     else:
#         p += line + ' '

#     if idx == len(input)-1:
#         fields = p.split(' ')[:-1] # discarding extra space at the end
#         passports += [[field[:3] for field in fields]]
#         p = ''

# valid_fields = set(['byr', 'iyr', 'eyr', 'ecl', 'pid', 'hcl', 'hgt'])
# valid = 0
# for p in passports:
#     if valid_fields.issubset(p):
#         valid += 1
# print(valid)

# part 2

passports = []
p = ''
for idx, line in enumerate(input):
    if line == '':
        fields = [field.split(':') for field in p.split(' ')[:-1]]
        passports += [[[f for f,v in fields], [v for f,v in fields]]]
        p = ''
    else:
        p += line + ' '

    if idx == len(input)-1:
        fields = [field.split(':') for field in p.split(' ')[:-1]]
        passports += [[[f for f,v in fields], [v for f,v in fields]]]
        p = ''

def valid_values(fields, values):
    for idx, field in enumerate(fields):
        val = values[idx]
        if field == 'byr':
            if not 1920 <= int(val) <= 2002:
                return False
        elif field == 'iyr':
            if not 2010 <= int(val) <= 2020:
                return False
        elif field == 'eyr':
            if not 2020 <= int(val) <= 2030:
                return False
        elif field == 'hgt':
            unit = val[-2:]
            if unit == 'cm':
                if not 150 <= int(val[:-2]) <= 193:
                    return False
            elif unit == 'in':
                if not 59 <= int(val[:-2]) <= 76:
                    return False
            else: 
                return False
        elif field == 'hcl':
            for idx, char in enumerate(val):
                if idx == 0 and char != '#':
                    return False
                elif idx != 0 and not char.isdigit() and char not in ['a', 'b', 'c', 'd', 'e', 'f']:
                    return False
        elif field == 'ecl':
            if val not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False
        elif field == 'pid':
            if len(val) != 9 or not val.isdigit():
                return False
    return True

valid_fields = set(['byr', 'iyr', 'eyr', 'ecl', 'pid', 'hcl', 'hgt'])
valid = 0
for fields, vals in passports:
    if valid_fields.issubset(fields) and valid_values(fields, vals):
        valid += 1

print(valid)
