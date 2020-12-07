import time
start_time = time.time()

import math


def decode(lowerChar, upperChar, boardingpass, min, max):
    for i in boardingpass:
        if i == lowerChar:
            max = int(math.floor(max - (max - min)/2))
        elif i == upperChar:
            min = int(math.floor(min + (max - min)/2))
    return max


file = open('resources/5_1_boardingpass.txt', 'r')
boardingPasses = file.read().split('\n')

maxSeatID = 0
for bp in boardingPasses:
    row = decode('F', 'B', bp[:8], 0, 127)
    seat = decode('L', 'R', bp[-3:], 0, 7)
    seatID = row * 8 + seat
    maxSeatID = seatID if seatID > maxSeatID else maxSeatID

print(maxSeatID)
print("--- %s seconds ---" % (time.time() - start_time))
