FILE_NAME = 'day14.txt'

lines = open(FILE_NAME).readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

# turning the grid so each row becomes a column
grid = []
for i in range(len(lines)):
    grid.append([lines[j][i] for j in range(len(lines[i]))])


# moving the rocks to the left side by counting
for i in range(len(grid)):
    prev = -1
    j = 0
    cnt = 0
    while j < len(grid[i]):
        if grid[i][j] == '#':
            if cnt == 0:
                prev = j
            else:
                for k in range(prev+1, prev+cnt+1):
                    grid[i][k] = 'O'
                for k in range(prev+cnt+1, j):
                    grid[i][k] = '.'
                cnt = 0
                prev = j

        elif grid[i][j] == 'O':
            cnt += 1

        j += 1

    if cnt > 0:
        for k in range(prev+1, prev+cnt+1):
            grid[i][k] = 'O'
        for k in range(prev+cnt+1, j):
            grid[i][k] = '.'

# counting the total rocks and their effect
total = 0
for line in grid:
    line = list(reversed(line))
    for i in range(len(line)):
        if line[i] == 'O':
            total += i+1

print(total)
