import time
import os
import re

USE_LOGGING = False
USE_DEMO = False
PART_ONE = False

def getInput(fileName):
    file = open(fileName, 'r')

    input = {int(line.split(':')[0][5:]): [[tuple(item.strip().split(' ')) for item in set.strip().split(',')] for set in line.split(':')[1].strip().split(';')] for line in file.readlines()}

    if USE_LOGGING: print(input)

    return input

def isSetPossible(maxRed, maxGreen, maxBlue, game):
    for set in game:
        for pull in set:
            count = int(pull[0])
            color = pull[1]

            if USE_LOGGING: print(f'\t{color}: {count}')

            # Had the idea later to reduce this to one line by storing the max values in a dictionary where the color value is the key.
            # Not gonna bother at this point
            match color:
                case 'red':
                    if count > maxRed: return False
                case 'green':
                    if count > maxGreen: return False
                case 'blue':
                    if count > maxBlue: return False

    return True

def getGameSum(input):
    sum = 0

    if PART_ONE:
        redMaximum = 12
        greenMaximum = 13
        blueMaximum = 14

        for key in input:
            if USE_LOGGING: print(f'Game {key}')

            if isSetPossible(redMaximum, greenMaximum, blueMaximum, input[key]): sum += key
    else:
        for key in input: # for some reason, input.items() is returning an object that includes the key instead of just the array that is the value
            highestRed, highestGreen, highestBlue = 0, 0, 0

            for set in input[key]:
                for pull in set: # turns out storing them in individual pulls wasn't necessary, could've reduced them all into a single array
                    count = int(pull[0])
                    color = pull[1]

                    match color:
                        case 'red':
                            highestRed = max(highestRed, count)
                        case 'green':
                            highestGreen = max(highestGreen, count)
                        case 'blue':
                            highestBlue = max(highestBlue, count)

            sum += highestRed * highestGreen * highestBlue

    return sum

startTime = time.time()

file = 'example.txt' if USE_DEMO else 'input1.txt'
input = getInput(file)
solution = getGameSum(input)

endtime = time.time()
print(f'Solution: ', solution)
print ('Completion time: ', endtime - startTime)