import time
from copy import deepcopy

USE_LOGGING = True
USE_DEMO = False
PART_ONE = False

def getInput(fileName):
    file = open(fileName, 'r')

    input = [[line.strip() for line in block.split('\n')] for block in file.read().split('\n\n')]

    return input

def rowsOffByOne(row1, row2):
    ob1 = False
    for j, c in enumerate(row1):
        if c != row2[j]:
            if ob1:
                return False
            else:
                ob1 = True

    return ob1

def checkReflection(pattern, rowNum, allowAdjustments):
    # I mixed symbolism here and used left/right instead of higher/lower, my bad
    lr, rr = rowNum, rowNum + 1 # initialize lr (left row) and rr (right row) indexes

    p = deepcopy(pattern)

    while lr >= 0 and rr < len(p): # while inside the bounds of the grid
        leftPattern, rightPattern = p[lr], p[rr] # get the left and right row values
        if leftPattern == rightPattern: # if they match, move the indexes out 1 and repeat
            lr = lr - 1
            rr += 1
        else: # they don't match
            if allowAdjustments: # if we're allowing adjustments (smudge correction)
                if rowsOffByOne(leftPattern, rightPattern): # if they're off by one
                    p[lr] = rightPattern # set the left pattern to the value of the right pattern
                    if checkReflection(p, rowNum, False): return True # if this produces a valid grid reflection (disallowing further adjustments) then this is a valid reflection

                    p[lr] = leftPattern # reset the left pattern to it's original value
                    p[rr] = leftPattern # set the right pattern to the value of the left pattern
                    return checkReflection(p, rowNum, False) # if this produces a valid grid reflection (disallowing further adjustments) then this is a valid reflection, otherwise this is not a valid reflection
                else: return False # they're not off by only one, this is an invalid reflection
            else: return False # no adjustments allowed, this is an invalid reflection
        
    return True # Didn't find any disqualifications, therefore it's a valid reflection

# blockLine represents a disallowed answer and is populated by the part 1 answer for the same grid
def getReflectionLine(pattern, rotate, blockLine):
    p = [''.join(list(reversed(x))) for x in zip(*pattern)] if rotate else deepcopy(pattern)
    
    for i, row in enumerate(p):
        if i+1 < len(p):
            nextRow = p[i+1]
            if row == nextRow:
                validReflection = checkReflection(p, i, blockLine is not None and not PART_ONE) # only allow adjustments if blockLine was provided and it's part two
                if validReflection and (PART_ONE or blockLine is None or blockLine != i):
                    return i # if line produces a valid grid reflection and it's either part one or blockline hasn't been provided or blockline isn't the same value as i, then this is the answer
            elif blockLine is not None and not PART_ONE: # if blockLine has been provided and it's not part one, then we can check for smudges/adjustments
                if rowsOffByOne(row, nextRow): # if the two rows are only off by one character
                    p[i] = nextRow # set this row to be the same as next row
                    if checkReflection(p, i, False) and blockLine != i:
                        return i # if this produces a valid grid reflection (disallowing further adjustments) and blockline isn't the same value as i, then this is the answer

                    p[i] = row # reset this row to it's original value
                    p[i+1] = row # set next row to be the same as this row

                    if checkReflection(p, i, False) and blockLine != i:
                        return i # if this produces a valid grid reflection (disallowing further adjustments) and blockline isn't the same value as i, then this is the answer
                    
                    p[i+1] = nextRow # reset the next row to it's original value

    return -1 # never found a row that produced a valid reflection

counter = 0
def getPatternValue(pattern):
    global counter
    counter += 1

    if USE_LOGGING: print(f'Checking pattern {counter}')
    hLine = getReflectionLine(pattern, False, None) # part 1 solution - horizontal reflection
    if USE_LOGGING: print(f'\thLine: {hLine}')
    if hLine >= 0 and PART_ONE: return (hLine + 1) * 100
    
    vLine = getReflectionLine(pattern, True, None) # part 1 solution - vertical reflection
    if USE_LOGGING: print(f'\tvLine: {vLine}')
    if vLine >= 0 and PART_ONE: return vLine + 1

    if not PART_ONE:
        hsLine = getReflectionLine(pattern, False, hLine) # part 2 solution - horizontal reflection
        if USE_LOGGING: print(f'\thsLine: {hsLine}')
        if hsLine >= 0 and hLine != hsLine: return (hsLine + 1) * 100
        
        vsLine = getReflectionLine(pattern, True, vLine) # part 2 solution - vertical reflection
        if USE_LOGGING: print(f'\tvsLine: {vsLine}')
        if vsLine >= 0 and vLine != vsLine: return vsLine + 1

    raise ValueError('No reflection line found')

startTime = time.time()

file = 'example.txt' if USE_DEMO else 'input1.txt'
input = getInput(file)
solution = sum([getPatternValue(p) for p in input])

endtime = time.time()
print(f'Solution: ', solution)
print ('Completion time: ', endtime - startTime)