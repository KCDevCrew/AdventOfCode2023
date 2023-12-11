import sys
file = open(sys.argv[1]).read().strip()

maxRed = 12
maxGreen = 13
maxBlue = 14

ans = 0

for lId,line in enumerate(file.split('\n')):
  # Find the first : and split the string into two parts
  # The first part is the key, the second part is the value
  key, value = line.split(':', 1)
  gameId = lId + 1
  value = value.strip()

  validGame = True
  
  # Split the drawings into a list
  for rId,round in enumerate(value.split(';')):
    # split the round into individual drawings
    for dId,drawing in enumerate(round.split(',')):
      drawing = drawing.strip()
      numCubes, cubeColor = drawing.split(' ')
      numCubes = int(numCubes)
      
      if cubeColor == 'red' and numCubes > maxRed:
        validGame = False
        break
      elif cubeColor == 'green' and numCubes > maxGreen:
        validGame = False
        break
      elif cubeColor == 'blue' and numCubes > maxBlue:
        validGame = False
        break

  if validGame == True:
    ans += gameId

print('ans:', ans) #2369