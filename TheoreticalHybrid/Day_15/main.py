import time

USE_LOGGING = False
USE_DEMO = False
PART_ONE = False

def getInput(fileName):
    file = open(fileName, 'r')

    input = [step.strip() for step in file.read().split(',')]

    if USE_LOGGING:
        for step in input: print(step)

    return input

def hashAlgorithm(input):
    value = 0

    for c in input:
        value = ((value + ord(c)) * 17) % 256

    return value

def hashMapAlgorithm(input):
    boxes = [[] for i in range(256)]

    for step in input:
        key, value = None, None
        if step[-1] == '-': key = step[:-1]
        else: key, value = step.split('=')

        keyHash = hashAlgorithm(key)
        boxValues = boxes[keyHash]
        existingLens = next((l for l in boxValues if l[0] == key), None)
        if value is None:
            if existingLens is not None: boxValues.remove(existingLens)
        else:
            if existingLens is not None:
                boxValues[boxValues.index(existingLens)] = (key, value)
            else: boxValues.append((key, value))

    focusPower = 0
    for i, b in enumerate(boxes):
        for j, l in enumerate(b):
            focusPower += (i+1)*(j+1)*int(l[1])

    return focusPower

startTime = time.time()

file = 'example.txt' if USE_DEMO else 'input1.txt'
input = getInput(file)
solution = sum(hashAlgorithm(step) for step in input) if PART_ONE else hashMapAlgorithm(input)

endtime = time.time()
print(f'Solution: ', solution)
print ('Completion time: ', endtime - startTime)