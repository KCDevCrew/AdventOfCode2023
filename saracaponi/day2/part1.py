import re

input = open('input.txt', 'r')
lines = input.readlines()

parsedGames = []

for games in lines:
    games = re.sub(r"[\n\t\s]*", "", games)
    reveals = games.split(':')[1].split(';')
    gameTotals = { 'red': 0, 'blue': 0, 'green': 0, 'possible': False}

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
    if game['red'] <= 12 and game['green'] <= 13 and game['blue'] <= 14:
        game['possible'] = True


count = 0
for idx, game in enumerate(parsedGames):
    if game['possible'] == True:
        count+= idx + 1


print(count)
