# Open the file
file = open('input.txt', 'r')
lines = file.readlines()
sum = 0
for line in lines:
  number = ''
  # Loop through the characters of the line, looking for the first number
  for char in line:
    if char.isnumeric():
      # If the character is numeric, append it and break the loop
      number += char
      break

  # Loop through the characters in reverse, looking for the last number
  for char in reversed(line):
    if char.isnumeric():
      # If the character is numeric, append it and break the loop
      number += char
      break

  # Add the number discovered to the sum
  sum += int(number)

print(sum)