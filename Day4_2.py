import time
start_time = time.time()

import re
FIELDS = ["byr",
          "iyr",
          "eyr",
          "hgt",
          "hcl",
          "ecl",
          "pid"]

def parse(data):
    return dict(field.split(':') for field in data.split())


def validate(passp):
    for f in FIELDS:
        field = passp.get(f)
        if field is None:
            return False
        if f == "byr":
            if 1920 > int(field) or int(field) > 2002:
                return False
        if f == "iyr":
            if 2010 > int(field) or int(field) > 2020:
                return False
        if f == "eyr":
            if 2020 > int(field) or int(field) > 2030:
                return False
        if f == "hgt":
            if field[-2:] == 'in':
                if 59 > int(field[:-2]) or int(field[:-2]) > 76:
                    return False
            elif field[-2:] == 'cm':
                if 150 > int(field[:-2]) or int(field[:-2]) > 193:
                    return False
            else:
                return False
        if f == "hcl":
            if re.search("#[a-f0-9]{6}", field) is None:
                return False
        if f == "ecl":
            if field not in {"amb","blu","brn","gry","grn","hzl","oth"}:
                return False
        if f == "pid":
            return str.isdigit(field) and len(field) == 9

    return True


with open("resources/4_1_passports.txt") as f:
    passports = [parse(fields) for fields in f.read().split('\n\n')]

VALID = 0
for passport in passports:
    if validate(passport):
        print(passport)
        VALID += 1

print(VALID)#127
print("--- %s seconds ---" % (time.time() - start_time))
