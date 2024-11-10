FILE_NAME = 'day07.txt'

lines = open(FILE_NAME).readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

class Card:

    # values of individual cards
    cardValues = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10
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

        # classifying the cards based on the rank
        if len(set(self.card)) == 1:
            return 7
        
        elif len(set(self.card)) == 5:
            return 1
        
        elif len(set(self.card)) == 4:
            return 2
        
        elif len(set(self.card)) == 3:
            if self.card.count(self.card[0]) == 3 or self.card.count(self.card[1]) == 3 or self.card.count(self.card[2]) == 3:
                return 4
            else:
                return 3
            
        elif len(set(self.card)) == 2:
            if self.card.count(self.card[0]) == 4 or self.card.count(self.card[0]) == 1:
                return 6
            else:
                return 5
        
    # overloaded lt operator to sort cards
    def __lt__(self, other):
        if self.rank == other.rank:
            for i in range(5):
                if self.card[i] != other.card[i]:
                    return self.cardValues[self.card[i]] < self.cardValues[other.card[i]]
            return False
        else:
            return self.rank < other.rank
        

# creating a list of cards
cards = []
for line in lines:
    cards.append(Card(line[:5:], line[6::]))

# sorting the cards
# and calculating the total bid based on the order
cards.sort()
total = 0
for i in range(len(cards)):
    total += cards[i].bid * (i + 1)

print(total)
