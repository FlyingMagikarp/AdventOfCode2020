import time
start_time = time.time()

import csv

MAP = []
TREE = '#'
ROUTES = [[1,1],
          [3,1],
          [5,1],
          [7,1],
          [1,2]]
TREES_TOTAL_ARR = []
TREES_TOTAL = 1

with open('resources/3_1_snowtrees.txt', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        MAP.append(row[0])

for r in ROUTES:
    COUNTER = 0
    X_AXIS_INC = r[0]
    Y_AXIS_INC = r[1]
    X_AXIS = 0-int(r[0])
    Y_AXIS = 0-int(r[1])

    while Y_AXIS < len(MAP)-1:
        X_AXIS += X_AXIS_INC
        Y_AXIS += Y_AXIS_INC
        X_AXIS = X_AXIS % len(MAP[Y_AXIS])
        if MAP[Y_AXIS][X_AXIS] == TREE:
            COUNTER += 1

    TREES_TOTAL_ARR.append(COUNTER)

for t in TREES_TOTAL_ARR:
    TREES_TOTAL = TREES_TOTAL * t

print(TREES_TOTAL_ARR)
print(TREES_TOTAL)
print("--- %s seconds ---" % (time.time() - start_time))
