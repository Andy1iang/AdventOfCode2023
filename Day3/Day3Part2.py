f = open('day03.txt', 'r')
doc = f.readlines()
for i in range(len(doc)):
    doc[i] = doc[i].strip()

lineLength = len(doc[0])
allNums = []

for lineIdx, line in enumerate(doc): #each line in document
    for letterIdx, letter in enumerate(line): #each letter in line
        if letter == '*':
            numsNear = 0 #keep track of amount of numbers near the *
            tempNums = [] #keep track of numbers near the *
            
            #getting left side of *
            if letterIdx > 0 and line[letterIdx-1].isdigit():
                numsNear += 1
                tempIdx = letterIdx-1
                tempNum = ''
                
                while tempIdx >= 0 and line[tempIdx].isdigit():
                    tempNum = line[tempIdx] + tempNum
                    tempIdx -= 1 
                tempNums.append(tempNum)
            
            #getting right side of *
            if letterIdx < lineLength-1 and line[letterIdx+1].isdigit():
                numsNear += 1
                tempIdx = letterIdx+1
                tempNum = ''
                
                while tempIdx < lineLength and line[tempIdx].isdigit():
                    tempNum = tempNum + line[tempIdx]
                    tempIdx +=1 
                tempNums.append(tempNum)
                
            if lineIdx != 0: #getting the line above
                leftIdx = letterIdx -1 
                if leftIdx<0:
                    leftIdx = 0
                rightIdx = letterIdx + 1 if letterIdx < lineLength-1 else letterIdx
                
                tempIdx = leftIdx
                while tempIdx <= rightIdx:
                    
                    if  tempIdx == leftIdx and tempIdx != 0 and doc[lineIdx-1][tempIdx].isdigit() and doc[lineIdx-1][tempIdx-1].isdigit():
                        numsNear += 1
                        tempNum = ''
                        while tempIdx >= 0 and doc[lineIdx-1][tempIdx].isdigit():
                            tempNum = doc[lineIdx-1][tempIdx] + tempNum
                            tempIdx -= 1 
                        tempIdx = leftIdx+1
                        while tempIdx < lineLength and doc[lineIdx-1][tempIdx].isdigit():
                            tempNum = tempNum + doc[lineIdx-1][tempIdx]
                            tempIdx +=1
                        tempNums.append(tempNum)
                        # print(doc[lineIdx-1][tempIdx])
                        # print(doc[lineIdx-1][tempIdx-1])
                    
                    elif doc[lineIdx-1][tempIdx].isdigit() and tempIdx <= rightIdx:
                        numsNear += 1
                        tempNum = ''
                        while tempIdx < lineLength and doc[lineIdx-1][tempIdx].isdigit():
                            tempNum = tempNum + doc[lineIdx-1][tempIdx]
                            tempIdx +=1
                        tempNums.append(tempNum)
                    
                    tempIdx += 1
            
            if lineIdx < len(doc)-1: #looking at line under
                leftIdx = letterIdx -1 
                if leftIdx<0:
                    leftIdx = 0
                rightIdx = letterIdx + 1 if letterIdx < lineLength-1 else letterIdx
                
                tempIdx = leftIdx
                while tempIdx <= rightIdx:
                    
                    if  tempIdx == leftIdx and tempIdx != 0 and doc[lineIdx+1][tempIdx].isdigit() and doc[lineIdx+1][tempIdx-1].isdigit() :
                        numsNear += 1
                        tempNum = ''
                        while tempIdx >= 0 and doc[lineIdx+1][tempIdx].isdigit():
                            tempNum = doc[lineIdx+1][tempIdx] + tempNum
                            tempIdx -= 1 
                        tempIdx = leftIdx+1
                        
                        while tempIdx < lineLength and doc[lineIdx+1][tempIdx].isdigit():
                            tempNum = tempNum + doc[lineIdx+1][tempIdx]
                            tempIdx +=1
                        tempNums.append(tempNum)
                    
                    elif doc[lineIdx+1][tempIdx].isdigit() and tempIdx <= rightIdx:
                        numsNear += 1
                        tempNum = ''
                        while tempIdx < lineLength and doc[lineIdx+1][tempIdx].isdigit():
                            tempNum = tempNum + doc[lineIdx+1][tempIdx]
                            tempIdx +=1
                        tempNums.append(tempNum)
                        
                    tempIdx += 1
                        
            
            if numsNear == 2:
                print(tempNums)
                newSum = 1
                for num in tempNums:
                    newSum *= int(num)
                allNums.append(newSum)

print(sum(allNums))