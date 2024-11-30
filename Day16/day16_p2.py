FILE_NAME = 'day16.txt'

grid = []
lines = open(FILE_NAME).readlines()
for i in range(len(lines)):
    grid.append(list(lines[i].strip()))

# same approach as part 1, but we are starting from all border cells


def getActivation(y, x, d):

    queue = []
    queue.append((y, x, d))

    seen = set()

    while queue:
        curr = queue.pop(0)
        while curr[0] >= 0 and curr[0] < len(grid) and curr[1] >= 0 and curr[1] < len(grid[0]) and (curr[0], curr[1], curr[2]) not in seen:
            y, x, d = curr
            sign = grid[y][x]
            seen.add((y, x, d))
            if sign == '.':
                if d == 'E':
                    curr = (y, x+1, d)
                elif d == 'W':
                    curr = (y, x-1, d)
                elif d == 'N':
                    curr = (y-1, x, d)
                elif d == 'S':
                    curr = (y+1, x, d)
            elif sign == '/':
                if d == 'E':
                    curr = (y-1, x, 'N')
                elif d == 'W':
                    curr = (y+1, x, 'S')
                elif d == 'N':
                    curr = (y, x+1, 'E')
                elif d == 'S':
                    curr = (y, x-1, 'W')
            elif sign == '\\':
                if d == 'E':
                    curr = (y+1, x, 'S')
                elif d == 'W':
                    curr = (y-1, x, 'N')
                elif d == 'N':
                    curr = (y, x-1, 'W')
                elif d == 'S':
                    curr = (y, x+1, 'E')
            elif sign == '-':
                if d == 'E':
                    curr = (y, x+1, d)
                elif d == 'W':
                    curr = (y, x-1, d)
                elif d == 'N' or d == 'S':
                    queue.append((y, x-1, 'W'))
                    queue.append((y, x+1, 'E'))
                    break
            elif sign == '|':
                if d == 'N':
                    curr = (y-1, x, d)
                elif d == 'S':
                    curr = (y+1, x, d)
                elif d == 'E' or d == 'W':
                    queue.append((y-1, x, 'N'))
                    queue.append((y+1, x, 'S'))
                    break

    coords = set()
    for s in seen:
        coords.add((s[0], s[1]))

    return len(coords)


# get all border cells' activations
activations = []
for y in range(len(grid)):
    activations.append(getActivation(y, 0, 'E'))
    activations.append(getActivation(y, len(grid[0])-1, 'W'))
for x in range(len(grid[0])):
    activations.append(getActivation(0, x, 'S'))
    activations.append(getActivation(len(grid)-1, x, 'N'))

# print the max activation
print(max(activations))
