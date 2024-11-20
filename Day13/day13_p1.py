FILE_NAME = 'day13.txt'

# lines contains a list of grids
lines = open(FILE_NAME).read().split('\n\n')
for i in range(len(lines)):
    lines[i] = lines[i].split()
    for j in range(len(lines[i])):
        lines[i][j] = lines[i][j].strip()

# checking for horizontal reflection


def horizontalReflection(grid, size):
    # for every possible mirror point
    # check outwards from there
    for i in range(size):
        offset = min(i, size-i-2)
        for j in range(offset+1):
            if grid[i-j] != grid[i+j+1]:
                break
        else:
            if i < size-1:
                return (i+1) * 100  # return the score

    return 0

# checking for verticle reflection


def verticalReflection(grid, size):
    # same approach as horizontal reflection
    # but splicing the grid instead of indexing (to deal with columns)
    for i in range(size):
        offset = min(i, size-i-2)
        for j in range(offset+1):
            left = [grid[k][i-j] for k in range(len(grid))]
            right = [grid[k][i+j+1] for k in range(len(grid))]
            if left != right:
                break
        else:
            if i < size-1:
                return i+1  # return the score

    return 0


# add to total score for each grid
total = 0
for grid in lines:
    total += horizontalReflection(grid, len(grid))
    total += verticalReflection(grid, len(grid[0]))

print(total)
