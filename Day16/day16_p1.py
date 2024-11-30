FILE_NAME = 'day16.txt'

grid = []
lines = open(FILE_NAME).readlines()
for i in range(len(lines)):
    grid.append(list(lines[i].strip()))

# queue to keep track of path we need to track
queue = []
queue.append((0, 0, 'E'))  # starting direction

# set to keep track of visited coordinates + direction it was headed
seen = set()

# while we still have path to track
while queue:

    # pop the first element in the queue
    curr = queue.pop(0)

    # while the current coordinate is within the grid and we haven't visited it yet
    while curr[0] >= 0 and curr[0] < len(grid) and curr[1] >= 0 and curr[1] < len(grid[0]) and (curr[0], curr[1], curr[2]) not in seen:
        y, x, d = curr
        sign = grid[y][x]  # get the sign at the current coordinate
        # add the current coordinate to the set of visited coordinates
        seen.add((y, x, d))

        # different cases for different signs
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
            # case where we need to split, we add new paths to the queue
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

# set to keep track of coordinates (we don't care about direction)
coords = set()
for s in seen:
    coords.add((s[0], s[1]))

print(len(coords))
