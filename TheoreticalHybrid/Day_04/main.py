import time
import os
import re
import math

USE_LOGGING = False
USE_DEMO = False
PART_ONE = False

def getInput(fileName):
    file = open(fileName, 'r')

    input = [[[int(number.strip()) for number in section.strip().split()] for section in line.split(':')[1].split('|')] for line in file.readlines()]

    if USE_LOGGING:
        for row in input:
            print(row)

    return input

def getCardPoints(winningNums, cardNumbers):
    winners = list(set(winningNums) & set(cardNumbers))

    return 0 if len(winners) == 0 else math.pow(2, len(winners) - 1)

def getTotalCardCount(input):
    totalCardCount = 0
    countList = [1]*len(input)

    for x, card in enumerate(input):
        thisCardCount = countList[x]
        if USE_LOGGING: print(f'(x{thisCardCount}) {card}')
        
        totalCardCount += thisCardCount
        winnerCount = len(list(set(card[0]) & set(card[1])))

        if winnerCount > 0:
            for i in range(1, winnerCount+1):
                countList[x+i] += thisCardCount

    return totalCardCount

startTime = time.time()

file = 'example.txt' if USE_DEMO else 'input1.txt'
input = getInput(file)
solution = sum([getCardPoints(card[0], card[1]) for card in input]) if PART_ONE else getTotalCardCount(input)

endtime = time.time()
print(f'Solution: ', solution)
print ('Completion time: ', endtime - startTime)