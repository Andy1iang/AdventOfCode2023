doc = open('Day7.txt', 'r').read().splitlines()

def sort_key(hands):
    cardRanks = 'AKQJT98765432'
    return (hands[0],cardRanks.find(hands[1][0]),cardRanks.find(hands[1][1]),cardRanks.find(hands[1][2]),cardRanks.find(hands[1][3]),cardRanks.find(hands[1][4]))

allHands = []

for line in doc:
    hand,point = line.split()
    cards = {}
    
    for card in hand:
        try:
            cards[card] += 1
        except KeyError:
            cards[card] = 1
    
    if len(cards) == 1:
        allHands.append((1,hand,point))
    elif len(cards) == 2:
        for key,value in cards.items():
            if value == 4 or value == 1:
                allHands.append((2,hand,point))
                break
            else:
                allHands.append((3,hand,point))
                break
    elif len(cards) == 3:
        for key,value in cards.items():
            if value == 3:
                allHands.append((4,hand,point))
                break
            elif value == 2:
                allHands.append((5,hand,point))
                break
    elif len(cards) == 4:
        allHands.append((6,hand,point))
    else:
        allHands.append((7,hand,point))
    

allHands.sort(key=sort_key,reverse=True)

total = 0

for i in range(len(allHands)):
    total += int(allHands[i][2]) * (i+1)

print(total)

        