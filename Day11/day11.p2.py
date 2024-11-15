FILE_NAME = 'day11.txt'

lines = open(FILE_NAME).readlines()
grid = []
for i in range(len(lines)):
    grid.append(list(lines[i].strip()))

# keeping track of rows and columns that are supposed to be duplicated
badRows = set()
badCols = set()
for i in range(len(grid)):
    if grid[i].count('#') == 0:
        badRows.add(i)
for i in range(len(grid[0])):
    if [grid[j][i] for j in range(len(grid))].count('#') == 0:
        badCols.add(i)

# finding all galaxies
galaxies = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '#':
            galaxies.append((i, j))


# for each path between two galaxies
# add 999999 to the total for each bad row or column in between
# the rows and columns with the galaxies will never be the bad ones
def countBadTrips(src, dst):
    cnt = 0
    for i in range(min(src[0], dst[0]), max(src[0], dst[0])):
        if i in badRows:
            cnt += 999999

    for i in range(min(src[1], dst[1]), max(src[1], dst[1])):
        if i in badCols:
            cnt += 999999

    return cnt


# for each pair of galaxies, calculate the distance between them
# and add the bad trips count to the total
total = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        total += abs(galaxies[i][0]-galaxies[j][0]) + \
            abs(galaxies[i][1]-galaxies[j][1])
        total += countBadTrips(galaxies[i], galaxies[j])

print(total)
