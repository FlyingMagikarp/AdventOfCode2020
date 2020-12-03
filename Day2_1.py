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
    i = r[3].count(r[2])
    if int(r[0]) <= i <= int(r[1]):
        COUNTER += 1

print(COUNTER)
print("--- %s seconds ---" % (time.time() - start_time))
