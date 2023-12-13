import time
from concurrent.futures import ThreadPoolExecutor

USE_LOGGING = True
USE_DEMO = False
PART_ONE = False

def getInput(fileName):
    file = open(fileName, 'r')

    input = [line for line in file.readlines()]

    return input

# Was used for debugging, not in use for solution
def checkSolution(proposed, map, rList):
    if len(proposed) != len(map):
        print(f'\t{proposed} is a different length than {map}')
        return False
    elif len(''.join(filter(lambda x: x == '#', proposed))) != sum(rList):
        print(f'\t{proposed} does not have the correct number of hashes ({sum(rList)}): {rList}')
        return False
    else:
        for i,c in enumerate(map):
            if c in ('.', '#'):
                if proposed[i] != c:
                    print(f'\t{map} expects a {c} at position [{i}] but {proposed} has a {proposed[i]}')
                    return False

        mapSections = []
        # I'm sure there's an easier way to do this, but here we go
        currentString = None
        for c in proposed:
            if currentString is None or currentString[-1] == c:
                currentString = c if currentString is None else currentString + c
            else:
                mapSections.append(currentString)
                currentString = c
        mapSections.append(currentString)

        listIndex = 0
        for section in mapSections:
            if section[0] == '#':
                if len(section) != rList[listIndex]:
                    print(f'\tList index {listIndex} expected a section of length {rList[listIndex]} but {proposed} has a section of length {len(section)}')
                    return False
                else:
                    listIndex += 1
    return True

PatternLookup = {}
def getPossibleArrangementCount(springMap, springList, prefix):
    global PatternLookup
    possibilities = 0

    localPrefix = prefix 

    key = (springMap, ','.join([str(sl) for sl in springList]))
    if key in PatternLookup:
        return PatternLookup[key]

    for i, c in enumerate(springMap):
        # if number of required characters (sum of springlist) + number of required characters between them (length of springList - 1) 
        # is greater than the remaining length of springMap, then it is impossible that springMap can satisfy the requirements of springList
        if sum(springList) + len(springList) - 1 > len(springMap) - i: break
        stopIndex = i+springList[0]
        if stopIndex > len(springMap): break
        if c in ('#', '?'):
            subString = springMap[i:stopIndex]
            if '.' not in subString and (stopIndex == len(springMap) or springMap[stopIndex] in ('.', '?')):
                if len(springList) == 1:
                    if '#' not in springMap[stopIndex:]: possibilities += 1
                    localPrefix += '.' if c == '?' else '#'
                else:
                    possibilities += getPossibleArrangementCount(springMap[stopIndex+1:], springList[1:], localPrefix + subString.replace('?', '#') + '.') # springMap[stopIndex+1:] is to cover the spacer character
                    localPrefix += '.' if c == '?' else '#'
                
                if subString[0] == '#':
                    break
            else:
                if c == '#': break
                else: localPrefix += '.'
        else: localPrefix += '.'

    PatternLookup[key] = possibilities
    return possibilities

def getPossibleArrangements(input):
    springMap, springList = input.strip().split()

    if not PART_ONE:
        springMap = '?'.join([springMap] * 5)
        springList = ','.join([springList] * 5)

    springList = [int(c) for c in springList.split(',')]
    #if USE_LOGGING: print(f'Checking {springMap} : {springList}')

    subTime = time.time()
    possibilities = getPossibleArrangementCount(springMap, springList, '')
    subEndTime = time.time()

    if USE_LOGGING: print(f'\t{springMap} has {possibilities} possibilities. Time: {subEndTime - subTime}')

    return possibilities

startTime = time.time()

file = 'example.txt' if USE_DEMO else 'input1.txt'
input = getInput(file)
solution = 0

with ThreadPoolExecutor() as executor:
    results = executor.map(getPossibleArrangements, input)
    solution = sum(results)

endtime = time.time()
print(f'Solution: ', solution)
print ('Completion time: ', endtime - startTime)