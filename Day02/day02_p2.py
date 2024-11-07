FILE_NAME = 'day02.txt'

lines = open(FILE_NAME).readlines()

total = 0

# same approach as part 1, but we each track of the minimum marbles of each color
for line in lines:
    info, marbles = line.split(':')
    info = int(info.split(' ')[1])

    # keeping track of the minimum marbles of each color
    minMarbles = {'red': 0, 'green': 0, 'blue': 0}
    for pull in marbles.split(';'):
        pull = pull.strip()
        for color in pull.split(','):
            color = color.strip()
            count, colorName = color.split(' ')
            # update the minimum number of marbles we need (highest we see)
            minMarbles[colorName] = max(minMarbles[colorName],int(count))

    # getting product of the minimum marbles of each color
    total += minMarbles['red'] * minMarbles['green'] * minMarbles['blue']

print(total)