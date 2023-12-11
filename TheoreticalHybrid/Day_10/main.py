import time

USE_LOGGING = False
USE_DEMO = False
PART_ONE = False

startingPoint = (0,0)
loop = []

def getInput(fileName):
    global startingPoint
    file = open(fileName, 'r')

    input = []
    
    for i,line in enumerate(file.readlines()):
        lineMap = []
        for j,c in enumerate(line.strip()):
            if c == 'S': startingPoint = (i,j)

            lineMap.append(c)
        input.append(lineMap)

    if USE_LOGGING:
        for line in input: print(line)

    return input

def moveLeft(c): # determine the next direction of movement if coming from the left
    match c:
        case '-':
            return 'l'
        case 'L':
            return 'u'
        case 'F':
            return 'd'

def moveRight(c): # determine the next direction of movement if coming from the right
    match c:
        case '-':
            return 'r'
        case '7':
            return 'd'
        case 'J':
            return 'u'

def moveUp(c): # determine the next direction of movement if coming from below
    match c:
        case '|':
            return 'u'
        case '7':
            return 'l'
        case 'F':
            return 'r'

def moveDown(c): # determine the next direction of movement if coming from above
    match c:
        case '|':
            return 'd'
        case 'L':
            return 'r'
        case 'J':
            return 'l'
        
def findFirstMove():
    myIndex = startingPoint
    ix, iy = myIndex[0], myIndex[1]
    if iy > 0 and input[ix][iy-1] in ('-', 'L', 'F'): # if starting point has a connecting pipe to the left
        return 'l'
    elif iy < len(input[0]) and input[ix][iy+1] in ('-', 'J', '7'): # if starting point has a connecting pipe to the right
        return 'r'
    elif ix > 0 and input[ix-1][iy] in ('|', '7', 'F'): # if starting point has a connecting pipe above
        return 'u'
    elif ix < len(input) and input[ix+1][iy] in ('|', 'L', 'J'): # if starting point has a connecting pipe below
        return 'd'

def buildLoop(input): # builds the global loop list and returns a new map that changes all non-loop characters to '.'
    global loop

    loop = [('S', startingPoint)]
    newInput = [['.'] * len(input[0]) for i in range(len(input))] # Build a new map that will be . except for the loop characters (cuts out the noise)

    d = findFirstMove()
    d1 = d # store for later pipe identification
    shifts = {'u': (-1, 0), 'd': (1, 0), 'r': (0, 1), 'l': (0, -1)}

    myIndex = startingPoint
    returnedToStart = False
    while not returnedToStart:
        s = shifts[d]
        sx, sy = myIndex[0] + s[0], myIndex[1] + s[1] # get the x,y for the next pipe
        sc = input[sx][sy] # get the next pipe
        loop.append((sc, (sx,sy))) # add next pipe to the loop as (pipeCharacter, (pipeX, pipeY))
        myIndex = (sx,sy)

        if sc == 'S': # if the next pipe is the starting point
            returnedToStart = True
            match d: # determine the underlying pipe depending on what direction took us here and what direction we started with
                case 'u':
                    match d1:
                        case 'u': sc = '|'
                        case 'r': sc = 'F'
                        case 'l': sc = '7'
                case 'd':
                    match d1:
                        case 'd': sc = '|'
                        case 'r': sc = 'L'
                        case 'l': sc = 'J'
                case 'r':
                    match d1:
                        case 'r': sc = '-'
                        case 'u': sc = 'J'
                        case 'd': sc = '7'
                case 'l':
                    match d1:
                        case 'l': sc = '-'
                        case 'u': sc = 'L'
                        case 'd': sc = 'F'
        else: # otherwise determine what direction the next pipe takes
            match d:
                case 'u':
                    d = moveUp(sc)
                case 'd':
                    d = moveDown(sc)
                case 'r':
                    d = moveRight(sc)
                case 'l':
                    d = moveLeft(sc)
        
        newInput[sx][sy] = sc # update new map with pipe character
    
    if USE_LOGGING: 
        for row in newInput: print(''.join(row))

    return newInput # return new map

def findEnclosedArea(input): # counts all '.' characters when it's between encasing pipe segments
    total = 0
    
    # evaluate each map character from top to bottom, left to right
    for row in input[1:-1]: # for each row besides the first and last (impossible to have valid '.' characters there)
        inside = False
        horizontalPipeEnd = None
        for c in row: # for each character in that row
            if c == '.':
                if inside:
                    total += 1
            elif c == '|': # '|' character always toggles the inside indicator
                inside = not inside
            else:
                if c in ('L', 'F'): # L and F always toggle the inside character
                    inside = not inside
                    horizontalPipeEnd = c # store the character as the beginning of a horizontal pipe segment
                
                # J and 7 only toggle the inside character if their vertical trajectory is different than that of the start of the horizontal pipe segment
                # For example, F---7 both have the vertical direction pointing downward, but F---J has F pointing downward but J pointing upward
                elif c in ('J', '7'):
                    inside = inside if horizontalPipeEnd == ('F' if c == 'J' else 'L') else not inside

    return total

startTime = time.time()

file = ('example1.txt' if PART_ONE else 'example2.txt') if USE_DEMO else 'input1.txt'
input = getInput(file)
input = buildLoop(input)

solution = len(loop) // 2 if PART_ONE else findEnclosedArea(input)

endtime = time.time()
print(f'Solution: ', solution)
print ('Completion time: ', endtime - startTime)