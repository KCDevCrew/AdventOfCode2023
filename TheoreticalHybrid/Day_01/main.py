import time
import os
import re

USE_LOGGING = False
USE_DEMO = False
PART_ONE = False

def getInput(fileName):
    file = open(fileName, 'r')
    input =  [x for x in file.read().split("\n")]

    if USE_LOGGING: print(input)

    return input

def getCalibrationSum(input):
    sum = 0

    if PART_ONE:
        for line in input:
            digit = (re.findall('\\d', line)[0]) + (re.findall('\\d', line[::-1])[0])
            sum += int(digit)
    else:
        textmap = {
            'one'   : '1',
            'two'   : '2',
            'three' : '3',
            'four'  : '4',
            'five'  : '5',
            'six'   : '6',
            'seven' : '7',
            'eight' : '8',
            'nine'  : '9'
        }

        for line in input:
            searchResults = re.findall('(?=(one|two|three|four|five|six|seven|eight|nine|\\d))', line) # Damn overlaps, need a lookahead
            
            digit1 = searchResults[0] if searchResults[0].isdigit() else textmap[searchResults[0]]
            digit2 = searchResults[-1] if searchResults[-1].isdigit() else textmap[searchResults[-1]]
            
            if USE_LOGGING: print(f'{searchResults}: {digit1 + digit2}')

            sum += int(digit1 + digit2)

    return sum

startTime = time.time()

file = 'example.txt' if USE_DEMO else 'input1.txt'
input = getInput(file)
solution = getCalibrationSum(input)

endtime = time.time()
print(f'Solution: ', solution)
print ('Completion time: ', endtime - startTime)