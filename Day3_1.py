import time
start_time = time.time()

import csv

MAP = []
COUNTER = 0
X_AXIS_INC = 3
Y_AXIS_INC = 1
X_AXIS = -3
Y_AXIS = -1
TREE = '#'

with open('resources/3_1_snowtrees.txt', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        MAP.append(row[0])

while Y_AXIS < len(MAP)-1:
    X_AXIS += X_AXIS_INC
    Y_AXIS += Y_AXIS_INC
    X_AXIS = X_AXIS % len(MAP[Y_AXIS])
    if MAP[Y_AXIS][X_AXIS] == TREE:
        COUNTER += 1


print(COUNTER)
print("--- %s seconds ---" % (time.time() - start_time))
