FILE_NAME = 'day03.txt'

lines = open(FILE_NAME).readlines()
for i in range(len(lines)): 
    lines[i] = lines[i].strip() # removes the newline characters

number = '' # stores the current number we're looking at
added = False # if we should add the number
total = 0

# looping through each line
for i in range(len(lines)):
    for j in range(len(lines[i])):

        # concatenating the number
        if lines[i][j].isnumeric():
            number += lines[i][j]

            # checking if we should add the number
            if not added:
                if j-1 >= 0 and not lines[i][j-1].isnumeric() and lines[i][j-1] != '.':
                    added = True
                elif i-1 >= 0 and not lines[i-1][j].isnumeric() and lines[i-1][j] != '.':
                    added = True
                elif j+1 < len(lines[i]) and not lines[i][j+1].isnumeric() and lines[i][j+1] != '.':
                    added = True
                elif i+1 < len(lines) and not lines[i+1][j].isnumeric() and lines[i+1][j] != '.':
                    added = True
                elif j-1 >= 0 and i-1 >= 0 and not lines[i-1][j-1].isnumeric() and lines[i-1][j-1] != '.':
                    added = True
                elif j+1 < len(lines[i]) and i-1 >= 0 and not lines[i-1][j+1].isnumeric() and lines[i-1][j+1] != '.':
                    added = True
                elif j-1 >= 0 and i+1 < len(lines) and not lines[i+1][j-1].isnumeric() and lines[i+1][j-1] != '.':
                    added = True
                elif j+1 < len(lines[i]) and i+1 < len(lines) and not lines[i+1][j+1].isnumeric() and lines[i+1][j+1] != '.':
                    added = True

        # once we reach a non-numeric character, we add the number if we should
        else:
            if added:
                total += int(number)
            added = False
            number = ''

    # at the end of each line
    if added:
        total += int(number)
    added = False
    number = ''

print(total)
