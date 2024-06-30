f = open('Day3.txt', 'r')
doc = f.readlines()
for i in range(len(doc)):
    doc[i] = doc[i].strip()

lineLength = len(doc[0])
allNums = []

for lineNum,line in enumerate(doc):
    for idx, letter in enumerate(line):
        if letter.isdigit() and (idx == lineLength-1 or not line[idx+1].isdigit()):
            num = letter
            tempIdx = idx
            while tempIdx != 0 and line[tempIdx-1].isdigit():
                num = line[tempIdx-1] + num
                tempIdx -= 1

            symbol = False
            leftIdx = tempIdx - 1
            rightIdx = idx + 1
            if tempIdx == 0:
                leftIdx+=1
            if idx == lineLength-1:
                rightIdx-=1
            
            for i in range(leftIdx, rightIdx+1):
                if symbol is True:
                    break
                
                if lineNum != 0:
                    if doc[lineNum-1][i] not in '0123456789.':
                            symbol = True
                if lineNum != (len(doc)-1):
                    if doc[lineNum+1][i] not in '0123456789.':
                            symbol = True
                if doc[lineNum][i] not in '0123456789.':
                            symbol = True
            
                
            if symbol:
                allNums.append(int(num))

print(sum(allNums))
                
