FILE_NAME = 'day11.txt'

lines = open(FILE_NAME).readlines()
grid = []
for i in range(len(lines)):
    grid.append(list(lines[i].strip()))

# doubling the empty universe rows backwards (avoid messing up index)
for i in range(len(grid)-1, -1, -1):
    if grid[i].count('#') == 0:
        grid.insert(i+1, grid[i])

# also doing it for the columns
for i in range(len(grid[0])-1, -1, -1):
    if [grid[j][i] for j in range(len(grid))].count('#') == 0:
        for j in range(len(grid)):
            grid[j].insert(i+1, grid[j][i])


# finding all the galaxies
galaxies = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '#':
            galaxies.append((i, j))

# calculating the total distance between each pair of galaxies (dx + dy)
total = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        total += abs(galaxies[i][0]-galaxies[j][0]) + \
            abs(galaxies[i][1]-galaxies[j][1])

print(total)
