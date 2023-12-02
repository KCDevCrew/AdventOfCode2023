import re

input = open('input.txt', 'r')
lines = input.readlines()

parsedGames = []

for games in lines:
    games = re.sub(r"[\n\t\s]*", "", games)
    reveals = games.split(':')[1].split(';')
    gameTotals = { 'red': 0, 'blue': 0, 'green': 0, 'cubed': 0}

    for reveal in reveals:
        blocks = reveal.split(',')

        for block in blocks:
            blockSplit = re.findall(r'\d+|\D+', block)
         
            amount = int(blockSplit[0])
            color = blockSplit[1]
            if amount > gameTotals[color]:
                gameTotals[color] = amount

    parsedGames.append(gameTotals)

for game in parsedGames:
    game['cubed'] = game['red'] * game['blue'] * game['green']


result = 0
for game in parsedGames:
    result+= game['cubed']

print(result)
