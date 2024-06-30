f = open("Day1.txt", "r")
doc = f.readlines()
numSet = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

allSums = 0

for line in doc:
    tempNums = []
    for index,letter in enumerate(line):
        if letter.isdigit():
            tempNums.append(letter)
        else:
            try:
                if line[index:index+3] in numSet.keys():
                    tempNums.append(numSet[line[index:index+3]])
                elif line[index:index+4] in numSet.keys():
                    tempNums.append(numSet[line[index:index+4]])
                elif line[index:index+5] in numSet.keys():
                    tempNums.append(numSet[line[index:index+5]])
            except IndexError:
                pass
                
    if len(tempNums) >= 1:
        allSums += int(tempNums[0]+tempNums[-1])

print(allSums)