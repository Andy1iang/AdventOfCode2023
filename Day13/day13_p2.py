FILE_NAME = 'day13.txt'

lines = open(FILE_NAME).read().split('\n\n')
for i in range(len(lines)):
    lines[i] = lines[i].split()
    for j in range(len(lines[i])):
        lines[i][j] = lines[i][j].strip()


# same approach as part 1
# except we only add the score if there is exactly one smudge(difference in the reflection)
def horizontalReflection(grid, size):
    for i in range(size):
        smudge = []
        offset = min(i, size-i-2)
        for j in range(offset+1):
            for k in range(len(grid[0])):
                if grid[i-j][k] != grid[i+j+1][k]:
                    smudge.append(i)

        if len(smudge) == 1:
            return (i+1) * 100

    return 0


def verticalReflection(grid, size):
    for i in range(size):
        smudge = []
        offset = min(i, size-i-2)
        for j in range(offset+1):
            for k in range(len(grid)):
                if grid[k][i-j] != grid[k][i+j+1]:
                    smudge.append(i)

        if len(smudge) == 1:
            return i+1

    return 0


total = 0
for grid in lines:
    total += horizontalReflection(grid, len(grid))
    total += verticalReflection(grid, len(grid[0]))

print(total)
