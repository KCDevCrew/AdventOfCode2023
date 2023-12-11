import time
from math import gcd

USE_LOGGING = False
USE_DEMO = False
PART_ONE = False

def getInput(fileName):
    file = open(fileName, 'r')

    inputData = file.read().split('\n\n')
    instructions = inputData[0]
    network = {}

    for mapping in inputData[1].split('\n'):
        key, value = mapping.strip().split('=')
        key = key.strip()
        value = value.strip()[1:-1].split(',')
        network[key] = (value[0].strip(), value[1].strip())

    input = (instructions, network)

    if USE_LOGGING: print(input)

    return input

def getStepCount(input):
    stepCount = 0

    endReached = False
    currentLocation = 'AAA'

    while not endReached:
        for instruction in input[0]:
            if currentLocation == 'ZZZ':
                endReached = True
                break

            nextLocation = input[1][currentLocation][0 if instruction == 'L' else 1]
            stepCount += 1
            currentLocation = nextLocation

    return stepCount

# I could probably augment getStepCount() to do both, but I don't feel like thinking too hard about it today
# Nevermind, doing it the same way is not viable
def getSimultaneousStepCount(input):
    stepCount = 0

    currentLocations = []
    for key in input[1]:
        if key[-1] == 'A':
            currentLocations.append(key)

    # Through some testing, discovered that each one has it's own perfect loop, so if it takes x steps to get to a location that ends with Z, it will take x steps to get to another one that ends with z
    # Because of this, I think I just need to find the least common multiple

    routeLengths = []

    for l in currentLocations:
        currentLocation = l
        endReached = False
        while not endReached:
            for instruction in input[0]:
                if currentLocation[-1] == 'Z':
                    routeLengths.append(stepCount)
                    endReached = True
                    break

                nextLocation = input[1][currentLocation][0 if instruction == 'L' else 1]
                stepCount += 1
                currentLocation = nextLocation
        stepCount = 0

    lcm = 1
    for length in routeLengths:
        lcm = lcm * length // gcd(lcm, length)

    return lcm

startTime = time.time()

file = ('example1.txt' if PART_ONE else 'example2.txt') if USE_DEMO else 'input1.txt'
input = getInput(file)
solution = getStepCount(input) if PART_ONE else getSimultaneousStepCount(input)

endtime = time.time()
print(f'Solution: ', solution)
print ('Completion time: ', endtime - startTime)