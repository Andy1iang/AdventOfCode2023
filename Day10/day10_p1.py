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

curr = start

# getting starting direction
direction = ''
if grid[start[0] - 1][start[1]] in 'F7|':
    direction = 'N'
    curr = [start[0] - 1, start[1]]
elif grid[start[0] + 1][start[1]] in 'JL|':
    direction = 'S'
    curr = [start[0] + 1, start[1]]
elif grid[start[0]][start[1] - 1] in 'LF-':
    direction = 'W'
    curr = [start[0], start[1] - 1]
elif grid[start[0]][start[1] + 1] in 'J7-':
    direction = 'E'
    curr = [start[0], start[1] + 1]

# finding the length of the path
pathLen = 1

while grid[curr[0]][curr[1]] != 'S':
    pathLen += 1
    x, y, direction = directions[grid[curr[0]][curr[1]]][direction]
    curr = [curr[0] + x, curr[1] + y]


print(pathLen//2)
