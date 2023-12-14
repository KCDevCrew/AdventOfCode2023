import time
import re
from copy import deepcopy
from collections import deque

USE_LOGGING = False
USE_DEMO = False
PART_ONE = False

def getInput(fileName):
    file = open(fileName, 'r')

    input = [line.strip() for line in file.readlines()]

    if USE_LOGGING:
        for line in input: print(line)

    return input

def rotateGrid(grid):
    return [''.join(list(reversed(x))) for x in zip(*grid)] # rotate it 90 degrees

def getLoad(grid, spinCount):
    counter = 0

    gridHistory = [deepcopy(grid)]

    compass = deque(['E', 'N', 'W', 'S']) # First element indicates what direction the right side of a row represents
    while counter < spinCount:
        grid = rotateGrid(grid)

        compass.rotate(-1)
        counter += 1
        if USE_LOGGING: print(counter)

        newGrid = []
        for row in grid:
            shifted = ''
            for sub in re.split('(#)', row): # split on the # character, but keeping the # character
                shifted += '#' if sub == '#' else ''.join(sorted(sub)) # if not #, then sort. This changes O..O.O to ...OOO
            newGrid.append(shifted)

        grid = newGrid

        for j,g in enumerate(gridHistory):
            foundMatch = True
            for i,r in enumerate(grid):
                if r != g[i]:
                    foundMatch = False
                    break
            if foundMatch: 
                #print(f'FOUND A GRID MATCH ({j}) AFTER {counter} SPINS')
                cycle = counter - j # determines the size of the cycle
                eq = (spinCount - j) % cycle # Determines how far past the cycle reset point is the spinCount value
                scGridIx = j + eq # The starting index of the cycle (j) + the spinCount offset (eq) will give us the matching grid for iteration spinCount
                compass.rotate(-1 * (counter - scGridIx)) # rotate the compass to match what direction the grid would be facing at iteration spinCount
                grid = gridHistory[scGridIx] # set the grid to what it would be at iteration spinCount
                counter = spinCount # short circuit the while loop
                break
            
        gridHistory.append(deepcopy(newGrid))

    while compass[0] != 'N':
        grid = rotateGrid(grid)
        compass.rotate(-1)

    load = 0
    for row in grid:
        if USE_LOGGING: print(row)
        load += sum([i+1 for i, c in enumerate(row) if c == 'O']) # calculates the total load on the north beams

    return load        

startTime = time.time()

file = 'example.txt' if USE_DEMO else 'input1.txt'
input = getInput(file)
solution = getLoad(input, 1 if PART_ONE else 4000000000)

endtime = time.time()
print(f'Solution: ', solution)
print ('Completion time: ', endtime - startTime)