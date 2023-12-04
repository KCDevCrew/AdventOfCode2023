import re

file1 = open('input.txt', 'r')
calibrationValues = file1.readlines()
 
numbers = []
numberMap = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
# create regex patter to match on number words or digit
regex_pattern = '|'.join(map(re.escape, numberMap.keys())) + '|\d' 

def map_number(num):
    if num.isdigit(): 
        return num
    else: 
        return numberMap[num]

for val in calibrationValues:
    parsedVals = re.findall("(?=(% s))" % regex_pattern, val)
    result = list(map(map_number, parsedVals))
    numbers.append(int(result[0] + result[-1]))

print(numbers)
print(sum(numbers))
