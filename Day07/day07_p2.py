FILE_NAME = 'day07.txt'

lines = open(FILE_NAME).readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

# same concept as part 1, but different way to find rank of cards
class Card:

    # Jack is now the lowest individual value
    # Jack can be used as any card to boost rank
    cardValues = {'A': 14, 'K': 13, 'Q': 12, 'J': -1, 'T': 10
                  , '9': 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}

    def __init__(self, card, bid):
        self.card = card
        self.bid = int(bid)
        self.rank = self.computeRank()

    def computeRank(self):
        # five of a kind: 7
        # four of a kind: 6
        # full house: 5
        # three of a kind: 4
        # two pairs: 3
        # one pair: 2
        # high card: 1

        # count number of jacks
        # if there are 4 or 5 jacks, then it is automatically five of a kind
        jokerCount = self.card.count('J')
        if jokerCount == 4 or jokerCount == 5:
            return 7
        
        # remove Jacks from card and count number of each card
        tempCard = self.card.replace('J', '')
        cardCounts = {}
        for card in tempCard:
            if card in cardCounts:
                cardCounts[card] += 1
            else:
                cardCounts[card] = 1

        # sort card counts in descending order
        cardCounts = list(cardCounts.values())
        cardCounts.sort(reverse=True)
        # add jokers to the highest count (creates highest rank possible)
        cardCounts[0] += jokerCount

        # getting card ranks
        if cardCounts[0] == 5:
            return 7
        elif cardCounts[0] == 4:
            return 6
        elif cardCounts[0] == 3:
            if cardCounts[1] == 2:
                return 5
            else:
                return 4
        elif cardCounts[0] == 2:
            if cardCounts[1] == 2:
                return 3
            else:
                return 2
        else:
            return 1
        
    def __lt__(self, other):
        if self.rank == other.rank:
            for i in range(5):
                if self.card[i] != other.card[i]:
                    return self.cardValues[self.card[i]] < self.cardValues[other.card[i]]
            return False
        else:
            return self.rank < other.rank
        

cards = []
for line in lines:
    cards.append(Card(line[:5:], line[6::]))

cards.sort()
total = 0
for i in range(len(cards)):
    total += cards[i].bid * (i + 1)

print(total)
