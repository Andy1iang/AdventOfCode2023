FILE_NAME = 'day14.txt'

lines = open(FILE_NAME).readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

# separating the grid into 2D array
grid = []
for i in range(len(lines)):
    grid.append(list(lines[i]))

# function to tilt the grid 4 times (north, west, south, east)


def tilt(grid):

    # north
    for i in range(len(grid[0])):
        prev = -1
        cnt = 0
        for j in range(len(grid)):
            if grid[j][i] == '#':
                if cnt == 0:
                    prev = j
                else:
                    for k in range(prev+1, prev+cnt+1):
                        grid[k][i] = 'O'
                    for k in range(prev+cnt+1, j):
                        grid[k][i] = '.'
                    cnt = 0
                    prev = j

            elif grid[j][i] == 'O':
                cnt += 1
        if cnt > 0:
            for k in range(prev+1, prev+cnt+1):
                grid[k][i] = 'O'
            for k in range(prev+cnt+1, len(grid)):
                grid[k][i] = '.'

    # west
    for i in range(len(grid)):
        prev = -1
        cnt = 0
        for j in range(len(grid[i])):
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

        if cnt > 0:
            for k in range(prev+1, prev+cnt+1):
                grid[i][k] = 'O'
            for k in range(prev+cnt+1, len(grid[i])):
                grid[i][k] = '.'

    # south
    for i in range(len(grid[0])):
        prev = len(grid)
        cnt = 0
        for j in range(len(grid)-1, -1, -1):
            if grid[j][i] == '#':
                if cnt == 0:
                    prev = j
                else:
                    for k in range(prev-1, prev-cnt-1, -1):
                        grid[k][i] = 'O'
                    for k in range(prev-cnt-1, j, -1):
                        grid[k][i] = '.'
                    cnt = 0
                    prev = j

            elif grid[j][i] == 'O':
                cnt += 1

        if cnt > 0:
            for k in range(prev-1, prev-cnt-1, -1):
                grid[k][i] = 'O'
            for k in range(prev-cnt-1, -1, -1):
                grid[k][i] = '.'

    # east
    for i in range(len(grid)):
        prev = len(grid[i])
        cnt = 0
        for j in range(len(grid[i])-1, -1, -1):
            if grid[i][j] == '#':
                if cnt == 0:
                    prev = j
                else:
                    for k in range(prev-1, prev-cnt-1, -1):
                        grid[i][k] = 'O'
                    for k in range(prev-cnt-1, j, -1):
                        grid[i][k] = '.'
                    cnt = 0
                    prev = j

            elif grid[i][j] == 'O':
                cnt += 1
        if cnt > 0:
            for k in range(prev-1, prev-cnt-1, -1):
                grid[i][k] = 'O'
            for k in range(prev-cnt-1, -1, -1):
                grid[i][k] = '.'


# keeping cache and index of each grid after tilting
cache = set(''.join([''.join(x) for x in grid]))
grids = [grid]

# tilting the grid until it reaches the same grid
i = 0
while i < 100000000:
    i += 1
    tilt(grid)
    key = ' '.join([''.join(x) for x in grid])
    if key in cache:
        break
    cache.add(key)
    grids.append(key)

# by then we will know we have encountered a loop
# so we find the offset of the first grid in the loop to when it loops
# then knowing the remainder of how many times it loops and add the offset to the remainder
first = grids.index(' '.join([''.join(x) for x in grid]))
grid = [list(j) for j in grids[(((1000000000 - first) %
                                 (i - first)) + first)].split(' ')]

# getting score
total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'O':
            total += (len(grid) - i)

print(total)
