import time

USE_LOGGING = False
USE_DEMO = False
PART_ONE = False

def getInput(fileName):
    file = open(fileName, 'r')
    input = [[int(c) for c in line.split()] for line in file.readlines()]
    if USE_LOGGING: print(input)
    return input

def getExtrapolatedValue(input):
    extrapolations = [input]
    allZeroes = False

    while not allZeroes:
        if not any(extrapolations[-1]): 
            allZeroes = True
            break

        newExtrapolation = []
        for a, b in zip(extrapolations[-1][:-1], extrapolations[-1][1:]):
            newExtrapolation.append(b - a)

        extrapolations.append(newExtrapolation)

    if USE_LOGGING: print(extrapolations)
    xValue = 0

    for xs in reversed(extrapolations[:-1]):
        if PART_ONE:
            xValue += xs[-1]
        else:
            xValue = xs[0] - xValue

    return xValue

startTime = time.time()

file = 'example.txt' if USE_DEMO else 'input1.txt'
input = getInput(file)
solution = sum([getExtrapolatedValue(line) for line in input])

endtime = time.time()
print(f'Solution: ', solution)
print ('Completion time: ', endtime - startTime)