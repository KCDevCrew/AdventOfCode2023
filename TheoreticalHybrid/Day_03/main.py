import time
import os
import re

USE_LOGGING = False
USE_DEMO = False
PART_ONE = False

def getInput(fileName):
    file = open(fileName, 'r')

    input = [[character for character in line.strip()] for line in file.readlines()]

    if USE_LOGGING:
        for row in input:
            print(row)

    return input

def hasQualifyingCharacter(testInput):
    for c in testInput:
        if not c.isdigit() and c != '.': return True

    return False

# check if it's adjacent to a non-period character
def numberIsValid(previousRow, thisRow, nextRow, startIndex, endIndex):
    yStart = startIndex
    if startIndex > 0:
        yStart = startIndex - 1
        if thisRow[yStart] != '.': return True

    yEnd = endIndex
    if endIndex < (len(thisRow)-1):
        yEnd = endIndex + 2 # +1 for the diagonal check and +1 because slicing is not inclusive
        if thisRow[endIndex + 1] != '.': return True

    return (previousRow and hasQualifyingCharacter(previousRow[yStart:yEnd])) or (nextRow and hasQualifyingCharacter(nextRow[yStart:yEnd]))

def getPartNumberSum(input):
    sum = 0

    for x, row in enumerate(input):
        numberString = ''
        yStart, yEnd = None, None
        for y, c in enumerate(row):
            if c.isdigit():
                if numberString == '':
                    yStart = y
                
                numberString += c
            else:
                if numberString != '': # don't forget you need to do this when reaching the end of a string too
                    yEnd = y-1
                    if USE_LOGGING: print(f'{numberString} at {x}:({yStart}-{yEnd})')

                    if numberIsValid(input[x-1] if x > 0 else None, row, input[x+1] if x < (len(input)-1) else None, yStart, yEnd):
                        if USE_LOGGING: print(f'{numberString} is valid')
                        sum += int(numberString)

                    numberString = ''

        if numberString != '':
            yEnd = len(row)-1

            if numberIsValid(input[x-1] if x > 0 else None, row, input[x+1] if x < (len(input)-1) else None, yStart, yEnd):
                if USE_LOGGING: print(f'{numberString} is valid')
                sum += int(numberString)

    return sum

def getNumber(row, startingY):
    numString = ''

    for c in row[startingY::-1]:
        if c.isdigit():
            numString += c
        else:
            break

    numString = numString[::-1]

    for c in row[startingY+1::]:
        if c.isdigit():
            numString += c
        else:
            break

    return numString

# short circuit at 3 since we know any more than 2 is an invalid character
def getAdjacentNumbers(input, gearX, gearY):
    adjNums = []

    xStart = gearX-1 if gearX > 0 else gearX
    xEnd = gearX+1 if gearX < (len(input)-1) else gearX
    yStart = gearY-1 if gearY > 0 else gearY
    yEnd = gearY+1 if gearY < (len(input[0])-1) else gearY
    
    # easy ones first
    if yStart < gearY and input[gearX][yStart].isdigit(): # number to the left of the *
        adjNums.append(getNumber(input[gearX], yStart))

    if yEnd > gearY and input[gearX][yEnd].isdigit(): # number to the right of the *
        adjNums.append(getNumber(input[gearX], yEnd))

    #row above
    if xStart < gearX:
        topLeftIsNumber = yStart < gearY and input[xStart][yStart].isdigit()
        topCenterIsNumber = input[xStart][gearY].isdigit()
        topRightIsNumber = yEnd > gearY and input[xStart][yEnd].isdigit()

        if (topLeftIsNumber and not topCenterIsNumber and topRightIsNumber): # brute forcing this case instead of trying to be clever about it in the loop
            adjNums.append(getNumber(input[xStart], yStart))
            adjNums.append(getNumber(input[xStart], yEnd))
        elif topLeftIsNumber or topCenterIsNumber or topRightIsNumber: # not necessary but a small short circuit
            for y in range(yStart, yEnd+1): # second number is exclusive
                if input[xStart][y].isdigit():
                    adjNums.append(getNumber(input[xStart], y))
                    break

    #row below
    if xEnd > gearX:
        bottomLeftIsNumber = yStart < gearY and input[xEnd][yStart].isdigit()
        bottomCenterIsNumber = input[xEnd][gearY].isdigit()
        bottomRightIsNumber = yEnd > gearY and input[xEnd][yEnd].isdigit()

        if (bottomLeftIsNumber and not bottomCenterIsNumber and bottomRightIsNumber): # brute forcing this case instead of trying to be clever about it in the loop
            adjNums.append(getNumber(input[xEnd], yStart))
            adjNums.append(getNumber(input[xEnd], yEnd))
        elif bottomLeftIsNumber or bottomCenterIsNumber or bottomRightIsNumber: # not necessary but a small short circuit
            for y in range(yStart, yEnd+1): # second number is exclusive
                if input[xEnd][y].isdigit():
                    adjNums.append(getNumber(input[xEnd], y))
                    break

    return adjNums

def getGearRatioSum(input):
    sum = 0

    for x, row in enumerate(input):
        for y, c in enumerate(row):
            if c == '*':
                # get adjacent numbers
                adjNums = getAdjacentNumbers(input, x, y)

                # if number of adjacent numbers is exactly 2, then multiply them together and that product to the sum
                if len(adjNums) == 2:
                    sum += (int(adjNums[0]) * int(adjNums[1]))

    return sum

startTime = time.time()

file = 'example.txt' if USE_DEMO else 'input1.txt'
input = getInput(file)
solution = getPartNumberSum(input) if PART_ONE else getGearRatioSum(input)

endtime = time.time()
print(f'Solution: ', solution)
print ('Completion time: ', endtime - startTime)