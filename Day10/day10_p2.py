FILE_NAME = 'day10.txt'

grid: list[list] = []

lines = open(FILE_NAME).readlines()
for i in range(len(lines)):
    grid.append(list(lines[i].strip()))

directions = {'J': {'E': (-1, 0, 'N'), 'S': (0, -1, 'W')}, 'F': {'W': (1, 0, 'S'), 'N': (0, 1, 'E')}, '7': {'E': (1, 0, 'S'), 'N': (0, -1, 'W')},
              'L': {'W': (-1, 0, 'N'), 'S': (0, 1, 'E')}, '|': {'N': (-1, 0, 'N'), 'S': (1, 0, 'S')}, '-': {'E': (0, 1, 'E'), 'W': (0, -1, 'W')}}

# finding starting position by location 'S'
start = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S':
            start = [i, j]

visited = set()
visited.add((start[0], start[1]))
curr = start

startSymbol = set(['-','|','F','J','7','L'])
# F 7 or L J should count has two (also if just one of them)
# F J or L 7 should count as one

# getting starting direction
direction = ''
if grid[start[0] - 1][start[1]] in 'F7|':
    direction = 'N'
    curr = [start[0] - 1, start[1]]
    startSymbol = startSymbol.difference(set(['F', '7', '-']))
if grid[start[0] + 1][start[1]] in 'JL|':
    direction = 'S'
    curr = [start[0] + 1, start[1]]
    startSymbol = startSymbol.difference(set(['L', 'J', '-']))
if grid[start[0]][start[1] - 1] in 'LF-':
    direction = 'W'
    curr = [start[0], start[1] - 1]
    startSymbol = startSymbol.difference(set(['L', 'F', '|']))
if grid[start[0]][start[1] + 1] in 'J7-':
    direction = 'E'
    curr = [start[0], start[1] + 1]
    startSymbol = startSymbol.difference(set(['J', '7', '|']))

startSymbol = list(startSymbol)[0]
print(startSymbol)

# finding the length of the path
pathLen = 1

while grid[curr[0]][curr[1]] != 'S':
    pathLen += 1
    visited.add((curr[0], curr[1]))
    x, y, direction = directions[grid[curr[0]][curr[1]]][direction]
    curr = [curr[0] + x, curr[1] + y]

grid[start[0]][start[1]] = startSymbol


def countCrossing(i, j):
    cnt = 0
    prev = ''
    for k in range(j):
        if not (i, k) in visited:
            continue
        if grid[i][k] in '|JL7F':
            if ((grid[i][k] == 'J' and prev == 'F') or (grid[i][k] == '7' and prev == 'L')):
                pass
            else:
                cnt += 1
            prev = grid[i][k]
    return int(cnt)


total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (i, j) not in visited:
            if countCrossing(i, j) % 2 == 1:
                total += 1

print(total)