import sys
file = open(sys.argv[1]).read().strip()

ans = 0

for lId,line in enumerate(file.split('\n')):
  key, value = line.split(':', 1)
  gameId = lId + 1
  value = value.strip()
  red = 0
  green = 0
  blue = 0  
  for rId,round in enumerate(value.split(';')):
    for dId,drawing in enumerate(round.split(',')):
      drawing = drawing.strip()
      numCubes, cubeColor = drawing.split(' ')
      numCubes = int(numCubes)
      if cubeColor == 'red' and numCubes > red:
        red = numCubes
      elif cubeColor == 'green' and numCubes > green:
        green = numCubes
      elif cubeColor == 'blue' and numCubes > blue:
        blue = numCubes

  ans += red * green * blue

print('ans:', ans) #66363