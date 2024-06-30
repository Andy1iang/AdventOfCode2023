f = open('Day4.txt', 'r')
doc = f.readlines()
total = 0

cards = {}
for i in range(len(doc)):
    cards[i] = 1

for lineIdx,line in enumerate(doc):
    
    tempLine = line.split(':')[1].strip()
    winning = tempLine.split('|')[0].strip()
    winning = winning.split()
    nums = tempLine.split('|')[1].strip()
    nums = nums.split()
    
    winning = set(winning)
    nums = set(nums)
    
    matches = winning.intersection(nums)
    
    for j in range(lineIdx+1,lineIdx+len(matches)+1):
        if j < len(doc):
            cards[j] += cards[lineIdx]
            
print(sum(cards.values()))