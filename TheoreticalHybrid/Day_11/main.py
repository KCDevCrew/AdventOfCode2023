import time

USE_LOGGING = False
USE_DEMO = False
PART_ONE = False

def getInput(fileName):
    global startingPoint
    file = open(fileName, 'r')

    input = [[c for c in line.strip()] for line in file.readlines()]

    if USE_LOGGING:
        for line in input: print(line)

    return input

def getShortestPaths(input):
    shortestPaths = []

    galaxies = []
    emptyRows = [True] * len(input)
    emptyColumns = [True] * len(input[0])

    for x,row in enumerate(input):
        for y,c in enumerate(row):
            if c == '#':
                galaxies.append((x,y))
                emptyRows[x] = False
                emptyColumns[y] = False

    for i,g in enumerate(galaxies):
        for g2 in galaxies[i+1:]:
            xDistance = 0
            for j in range(min(g[0], g2[0]) + 1, max(g[0], g2[0]) + 1):
                xDistance += (2 if PART_ONE else 1000000) if emptyRows[j] else 1

            yDistance = 0
            for j in range(min(g[1], g2[1]) + 1, max(g[1], g2[1]) + 1):
                yDistance += (2 if PART_ONE else 1000000) if emptyColumns[j] else 1

            shortestPaths.append(xDistance + yDistance)

    return shortestPaths

startTime = time.time()

file = 'example.txt' if USE_DEMO else 'input1.txt'
input = getInput(file)
solution = sum(getShortestPaths(input))

endtime = time.time()
print(f'Solution: ', solution)
print ('Completion time: ', endtime - startTime)