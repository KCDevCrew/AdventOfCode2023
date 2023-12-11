import time

USE_LOGGING = True
USE_DEMO = False
PART_ONE = False

def getInput(fileName):
    file = open(fileName, 'r')

    file = file.readlines()
    times = file[0].split(':')[1].strip().split()
    distances = file[1].split(':')[1].strip().split()

    if not PART_ONE:
        times = [''.join(times)]
        distances = [''.join(distances)]

    times = [int(t) for t in times]
    distances = [int(d) for d in distances]
    input = list(zip(times, distances))

    if USE_LOGGING: print(input)

    return input

def getRaceDistance(buttonHoldTime, maxTime):
    return buttonHoldTime * (maxTime - buttonHoldTime)

def ceilingSplit(num):
    return -(num // -2)

# going to try divide and conquer to find the bounds instead of brute forcing, as I expect part 2 to be a problem
# VALIDATION
def getWinningRaceBounds(time, distance):
    lowerBound, upperBound = None, None

    nextCheck, lastCheck = ceilingSplit(time), time
    nextRange = ceilingSplit(abs(lastCheck - nextCheck))
    
    while nextRange > 0:
        rd = getRaceDistance(nextCheck, time)
        nextRange = 0 if nextRange == 1 else ceilingSplit(abs(lastCheck - nextCheck))
        if rd > distance: # successful time input, check higher
            upperBound = nextCheck if upperBound is None else max(upperBound, nextCheck)
            lastCheck = nextCheck
            nextCheck = nextCheck + nextRange
        else: # unsuccessful time input, check lower
            lastCheck = nextCheck
            nextCheck = nextCheck - nextRange

    nextCheck, lastCheck = ceilingSplit(time), 0
    nextRange = ceilingSplit(abs(lastCheck - nextCheck))
    
    while nextRange > 0:
        rd = getRaceDistance(nextCheck, time)
        nextRange = 0 if nextRange == 1 else ceilingSplit(abs(lastCheck - nextCheck))
        if rd > distance: # successful time input, check lower
            lowerBound = nextCheck if lowerBound is None else min(lowerBound, nextCheck)
            lastCheck = nextCheck
            nextCheck = nextCheck - nextRange
        else: # unsuccessful time input, check higer
            lastCheck = nextCheck
            nextCheck = nextCheck + nextRange

    return (lowerBound, upperBound)

def getWinningOptions(input):
    winnerCounts = []

    for race in input:
        time, distance = race[0], race[1]
        winnerBounds = getWinningRaceBounds(time, distance)
        winnerCounts.append(winnerBounds[1] - winnerBounds[0] + 1)

        if USE_LOGGING: print(f'Lower: {winnerBounds[0]} | Upper: {winnerBounds[1]} | # Winners: {winnerBounds[1] - winnerBounds[0] + 1}')

    return winnerCounts

startTime = time.time()

file = 'example.txt' if USE_DEMO else 'input1.txt'
input = getInput(file)
solution = 1

winningCounts = getWinningOptions(input)
for c in winningCounts: solution = solution * c

endtime = time.time()
print(f'Solution: ', solution)
print ('Completion time: ', endtime - startTime)