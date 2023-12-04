# Open the file
file = open('input.txt', 'r')
lines = file.readlines()

strNumList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
strNumListReverse = []
for s in strNumList:
  strNumListReverse.append(s[::-1])

# print first line
line = lines[0]
sum = 0
for line in lines:
  line = line.strip()
  number = ''
  # Loop through the characters of the line, looking for the first number
  for i,char in enumerate(line):
    hit = False
    if char.isnumeric():
      # If the character is numeric, append it and break the loop
      number += char
      hit = True
    else:
      for d,strNum in enumerate(strNumList):
        if line[i:].startswith(strNum):
          number += str(d)
          hit = True
    if hit:
      break

  # Loop through the characters in reverse, looking for the last number
  reversedLine = line[::-1]
  for i,char in enumerate(reversedLine):
    hit = False
    if char.isnumeric():
      # If the character is numeric, append it and break the loop
      number += char
      hit = True
    else:
      for d,strNumR in enumerate(strNumListReverse):
        if reversedLine[i:].startswith(strNumR):
          number += str(d)
          hit = True
    if hit:
      break

  # Add the number discovered to the sum
  sum += int(number)

print(sum)