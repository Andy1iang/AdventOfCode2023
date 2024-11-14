FILE_NAME = 'day05.txt'

lines = open(FILE_NAME).readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

# testing lines
# SHIFT_LINES = [(3,5), (7,10), (12,16), (18,20), (22,25), (27,29), (31,33)]

# lines of the shifts
SHIFT_LINES = [(3, 47), (49, 71), (73, 113), (115, 158),
               (160, 194), (196, 241), (243, 277)]

# our initial seeds
seeds = list(map(int, lines[0][6::].split()))


def shiftSeeds(start, end):

    # getting the shifts
    shifts = []
    for i in range(start, end):
        shifts.append(list(map(int, lines[i].split())))

    # for each seeds
    # check if it's in the shift range
    # if it is, shift it
    for i in range(len(seeds)):
        for j in range(len(shifts)):
            if shifts[j][1] <= seeds[i] < (shifts[j][1] + shifts[j][2]):
                seeds[i] += (shifts[j][0] - shifts[j][1])
                break  # goto next seed if we shifted


# shifting seeds for each part of almanac
for i in range(len(SHIFT_LINES)):
    shiftSeeds(SHIFT_LINES[i][0], SHIFT_LINES[i][1])

print(min(seeds))
