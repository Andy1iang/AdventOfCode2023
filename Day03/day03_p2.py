FILE_NAME = 'day03.txt'

lines = open(FILE_NAME).readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

# returns the integer value of a number
# given the index of one of the digits


def getNum(i, j):
    # looks left
    t = j
    num = lines[i][j]
    while t-1 >= 0 and lines[i][t-1].isnumeric():
        num = lines[i][t-1] + num
        t -= 1

    # looks right
    while j+1 < len(lines[i]) and lines[i][j+1].isnumeric():
        num = num + lines[i][j+1]
        j += 1

    return int(num)


total = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):

        # when we find a character *
        if lines[i][j] == '*':

            ratios = []

            # checking left and right
            if j-1 >= 0 and lines[i][j-1].isnumeric():
                ratios.append(getNum(i, j-1))
            if j+1 < len(lines[i]) and lines[i][j+1].isnumeric():
                ratios.append(getNum(i, j+1))

            # checking the middle one on top
            if i-1 >= 0 and lines[i-1][j].isnumeric():
                ratios.append(getNum(i-1, j))
            # if it's not a number, check both left and right
            else:
                if j-1 >= 0 and i-1 >= 0 and lines[i-1][j-1].isnumeric():
                    ratios.append(getNum(i-1, j-1))
                if j+1 < len(lines[i]) and i-1 >= 0 and lines[i-1][j+1].isnumeric():
                    ratios.append(getNum(i-1, j+1))

            # same process for the bottom
            if i+1 < len(lines) and lines[i+1][j].isnumeric():
                ratios.append(getNum(i+1, j))
            else:
                if j-1 >= 0 and i+1 < len(lines) and lines[i+1][j-1].isnumeric():
                    ratios.append(getNum(i+1, j-1))
                if j+1 < len(lines[i]) and i+1 < len(lines) and lines[i+1][j+1].isnumeric():
                    ratios.append(getNum(i+1, j+1))

            # only add product if we have two ratios
            if len(ratios) == 2:
                total += ratios[0]*ratios[1]

print(total)
