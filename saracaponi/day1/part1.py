file1 = open('input.txt', 'r')
calibrationValues = file1.readlines()

numbers = []
for val in calibrationValues:
    for s in val.split():
        parsedValue = ''.join(filter(str.isdigit, s))
        numbers.append(int(parsedValue[0] + parsedValue[-1]))

print(numbers)
print(sum(numbers))
