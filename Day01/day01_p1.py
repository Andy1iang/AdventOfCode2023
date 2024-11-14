FILE_NAME = 'day01.txt'

lines = open(FILE_NAME).readlines()

total = 0
for line in lines:

    # concatenate the first and last numbers in the line
    temp = ''

    # looking from the front
    for i in range(len(line)):
        if line[i].isnumeric():
            temp += line[i]
            break

    # looking from the back
    for i in range(len(line)-1, -1, -1):
        if line[i].isnumeric():
            temp += line[i]
            break

    # add integer representation to total
    total += int(temp)

print(total)
