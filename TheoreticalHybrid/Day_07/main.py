import time

USE_LOGGING = False
USE_DEMO = False
PART_ONE = False

class CardHand:
    def __init__(self, cards, bid):
        self.OriginalHand = cards
        self.Bid = int(bid)

        self.TransformedHand = []
        self.HandLookup = {}

        jokerCount = 0
        for card in cards:
            cardValue = None
            if card.isdigit(): cardValue = int(card)
            else:
                match card:
                    case 'A': cardValue = 14
                    case 'K': cardValue = 13
                    case 'Q': cardValue = 12
                    case 'J': cardValue = 11 if PART_ONE else 1
                    case 'T': cardValue = 10

            self.TransformedHand.append(cardValue)

            if not PART_ONE and card == 'J':
                jokerCount += 1
            else:
                self.HandLookup[card] = self.HandLookup[card] + 1 if card in self.HandLookup else 1

        if jokerCount == 5:
            self.HandLookup['J'] = 5
        else:
            maxKey = max(self.HandLookup, key=self.HandLookup.get)
            self.HandLookup[maxKey] = self.HandLookup[maxKey] + jokerCount

    def __repr__(self):
        return f'Hand: {self.OriginalHand} | Transformed: {self.TransformedHand} | Lookup: {self.HandLookup}'

def getInput(fileName):
    file = open(fileName, 'r')

    input = [CardHand(line.split()[0], line.split()[1]) for line in file.readlines()]

    if USE_LOGGING:
        for hand in input:
            print(hand)

    return input

def getHandType(hand: CardHand):
    # Return a different value for each hand type

    numberUniqueCards = len(hand.HandLookup.keys())

    match numberUniqueCards:
        case 1:
            # If hand is 5 of a kind, return 1
            return 1
        case 2:
            # If hand is 4 of a kind, return 2
            # Else if hand is Full House, return 3
            firstValue = list(hand.HandLookup.values())[0]
            return 2 if firstValue == 1 or firstValue == 4 else 3 # If value is 1 or 4 that means it's a 4 of a kind, otherwise it's a full house
        case 3:
            # If hand is 3 of a Kind, return 4
            # Else if hand is 2 pair, return 5
            for value in hand.HandLookup.values():
                if value > 1: # For 3 unique cards, it's either 3/1/1 or 2/2/1
                    return 4 if value == 3 else 5 # If it's a 3, then it's 3 of a kind, otherwise it's 2 pair
        case 4:
            # Hand is 1 pair, return 6
            return 6
        case 5:
            # Hand is high card, return 7
            return 7
    
    pass

def getTotalWinnings(input: [CardHand]):
    winnings = 0

    handTypeDict = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    
    for hand in input:
        handType = getHandType(hand)

        if USE_LOGGING:
            print()
            print(hand)
            print(f'\t{handType}')

        handTypeDict[handType].append(hand)

    rank = 1
    for key in reversed(handTypeDict.keys()):
        sortedHands = sorted(handTypeDict[key], key=lambda h: h.TransformedHand)

        for sh in sortedHands:
            score = rank * sh.Bid
            if USE_LOGGING: print(f'\t{sh} | Winnings: {score}')
            winnings += score
            rank += 1

    return winnings

startTime = time.time()

file = 'example.txt' if USE_DEMO else 'input1.txt'
input = getInput(file)
solution = getTotalWinnings(input)

endtime = time.time()
print(f'Solution: ', solution)
print ('Completion time: ', endtime - startTime)