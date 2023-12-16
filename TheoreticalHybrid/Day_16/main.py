import time

USE_LOGGING = False
USE_DEMO = False
PART_ONE = False

EnergyMap = None
EnergyCounter = 0

def reset(input):
    global EnergyMap
    global EnergyCounter
    # Set up the energy map to be a grid of equal size with every element being an empty list. This will store every direction a beam has traveled on that tile.
    # This is to detect loops
    EnergyMap = [[[] for j in range(len(input[0]))] for i in range(len(input))]
    EnergyCounter = 0

def getInput(fileName):
    file = open(fileName, 'r')

    input = [[c for c in line.strip().replace('\\', 'b')] for line in file.readlines()] # replacing \ with b for backslash for the sake of more readable output
    reset(input)

    if USE_LOGGING:
        for step in input: print(step)

    return input

def energize(input, startingTile, direction):
    global EnergyMap
    global EnergyCounter

    x,y = startingTile
    splitList = []

    while 0 <= x < len(input[0]) and 0 <= y < len(input):
        tile = EnergyMap[y][x]
        if not tile: # if list is empty 
            EnergyCounter += 1
            tile.append(direction)     
        elif direction in tile:
            break # found a loop
        else:
            tile.append(direction)

        tileChar = input[y][x]
        if tileChar == '.':
            if direction in ('r', 'l'):
                x = x + 1 if direction == 'r' else x - 1
            else:
                y = y + 1 if direction == 'd' else y - 1
        elif tileChar == '|':
            if direction in ('r', 'l'):
                splitList.append(((x, y-1), 'u')) # add the up split to the queue to be parsed later
                # Continue this iteration going down
                y += 1
                direction = 'd'
            else:
                y = y + 1 if direction == 'd' else y - 1
        elif tileChar == '-':
            if direction in ('r', 'l'):
                x = x + 1 if direction == 'r' else x - 1
            else:
                splitList.append(((x-1, y), 'l')) # add the left split to the queue to be parsed later
                # Continue this iteration going right
                x += 1
                direction = 'r'
        elif tileChar in ('/', 'b'):
            slashChar = tileChar == '/'
            match direction:
                case 'r':
                    y = y - 1 if slashChar else y + 1
                    direction = 'u' if slashChar else 'd'
                case 'l':
                    y = y + 1 if slashChar else y - 1
                    direction = 'd' if slashChar else 'u'
                case 'u':
                    x = x + 1 if slashChar else x - 1
                    direction = 'r' if slashChar else 'l'
                case 'd':
                    x = x - 1 if slashChar else x + 1
                    direction = 'l' if slashChar else 'r'

    for s,d in splitList:
        energize(input, s, d)

startTime = time.time()

file = 'example.txt' if USE_DEMO else 'input1.txt'
input = getInput(file)

solution = 0

if PART_ONE:
    energize(input, (0,0), 'r')
    solution = EnergyCounter
else:
    maximumEffort = 0
    xRange = len(input[0])
    yRange = len(input)

    for y in range(yRange):
        energize(input, (0,y), 'r') # come in from the left side of the grid
        maximumEffort = max(maximumEffort, EnergyCounter)
        reset(input)
        energize(input, (xRange, y), 'l') # come in from the right side of the grid
        maximumEffort = max(maximumEffort, EnergyCounter)
        reset(input)

    for x in range(xRange):
        energize(input, (x,0), 'd') # come in from the top of the grid
        maximumEffort = max(maximumEffort, EnergyCounter)
        reset(input)
        energize(input, (x, yRange), 'u') # come in from the bottom of the grid
        maximumEffort = max(maximumEffort, EnergyCounter)

    solution = maximumEffort

endtime = time.time()
print(f'Solution: ', solution)
print ('Completion time: ', endtime - startTime)