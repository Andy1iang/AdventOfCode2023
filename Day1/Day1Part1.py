f = open("Day1.txt", "r")
doc = f.readlines()

allSums = 0

for line in doc:
    tempNums = []
    for letter in line:
        if letter.isdigit():
            tempNums.append(letter)

    if len(tempNums) >= 1:
        allSums += int(tempNums[0]+tempNums[-1])

print(allSums)