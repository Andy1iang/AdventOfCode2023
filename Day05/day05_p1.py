FILE_NAME = 'day05.txt'

lines = open(FILE_NAME).readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

SHIFT_LINES = [(3,5), (7,10), (12,16), (18,20), (22,25), (27,29), (31,33)]
seeds = list(map(int, lines[0][6::].split()))

def shiftSeeds(start, end):

    shifts = []
    for i in range(start, end):
        shifts.append(list(map(int, lines[i].split())))

    for i in range(len(seeds)):
        for j in range(len(shifts)):
            if shifts[j][1] <= seeds[i] < (shifts[j][1] + shifts[j][2]):
                seeds[i] += (shifts[j][0] - shifts[j][1])

    
for i in range(len(SHIFT_LINES)):
    shiftSeeds(SHIFT_LINES[i][0], SHIFT_LINES[i][1])
    print(seeds)

print(min(seeds))