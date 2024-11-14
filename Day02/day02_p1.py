FILE_NAME = 'day02.txt'

lines = open(FILE_NAME).readlines()

# limit on what
limits = {'red': 12, 'green': 13, 'blue': 14}

total = 0

# going through each line
for line in lines:

    # getting game id
    info, marbles = line.split(':')
    info = int(info.split(' ')[1])

    # going through each pull from each line
    add = True
    for pull in marbles.split(';'):
        pull = pull.strip()  # cleaning whitespace

        # going through each color in each pull
        for color in pull.split(','):
            color = color.strip()
            # if color exceeds limit, don't add to total
            if limits[color.split(' ')[1]] < int(color.split(' ')[0]):
                add = False
                break

    if add is True:
        total += info

print(total)
