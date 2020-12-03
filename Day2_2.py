import time
start_time = time.time()

import csv

PASSWORDS = []
COUNTER = 0
with open('resources/2_1_passwd.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        r = row[0].replace("-", " ")
        r = r.replace(":", "")

        PASSWORDS.append(r.split(" "))

for r in PASSWORDS:
    if r[3][int(r[0])-1] == r[2] or r[3][int(r[1])-1] == r[2]:
        if r[3][int(r[0])-1] != r[3][int(r[1])-1]:
            COUNTER += 1

print(COUNTER)
print("--- %s seconds ---" % (time.time() - start_time))
