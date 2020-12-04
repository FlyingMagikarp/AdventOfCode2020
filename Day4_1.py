import time
start_time = time.time()

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
    validPassp = True
    for f in FIELDS:
        if passp.get(f) is None:
            validPassp = False
    return validPassp


with open("resources/4_1_passports.txt") as f:
    passports = [parse(fields) for fields in f.read().split('\n\n')]

VALID = 0
for passport in passports:
    if validate(passport):
        VALID += 1

print(VALID)
print("--- %s seconds ---" % (time.time() - start_time))
