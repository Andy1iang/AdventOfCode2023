FILE_NAME = 'day05.txt'

lines = open(FILE_NAME).readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

# lines of the shifts (exclusive end)
SHIFT_LINES = [(3,47), (49,71), (73,113), (115,158), (160,194), (196,241), (243,277)]

# our initial seeds
seedsLine = list(map(int, lines[0][6::].split()))
seeds = []

# putting seeds in pairs
for i in range(len(seedsLine)//2):
    seeds.append([seedsLine[2*i], seedsLine[2*i]+seedsLine[(2*i)+1]])

def shiftSeeds(start, end):

    # getting the shifts
    shifts = []
    for i in range(start, end):
        shifts.append(list(map(int, lines[i].split())))

    # while loop to account for new seeds added
    i = 0
    while i < len(seeds):
        for dst, src, spr in shifts:
            # if both ends are encapsulating range
            # create new seed range on both ends and shift the middle
            if seeds[i][0] < src and seeds[i][1] >= (src+spr):
                seeds.append([seeds[i][0], src-1])
                seeds.append([src+spr, seeds[i][1]])
                seeds[i] = [dst, dst+spr]
                break

            # if both in bounds
            # shift the seed range
            elif seeds[i][0] >= src and seeds[i][1] < (src+spr):
                seeds[i][0] += (dst-src)
                seeds[i][1] += (dst-src)
                break

            # if right side is out of bounds
            # create new seed range on the right side
            # and shift the left side
            elif seeds[i][0] < (src+spr) and seeds[i][1] >= (src+spr):
                seeds.append([src+spr, seeds[i][1]])
                seeds[i][0] += (dst-src)
                seeds[i][1] = (dst+spr)
                break

            # if left end is in bounds
            # create new seed range on the left side
            # and shift the right side
            elif seeds[i][0] < src and seeds[i][1] >= (src+spr):
                seeds.append([seeds[i][0], src-1])
                seeds[i][0] = (dst)
                seeds[i][1] += (dst-src)
                break

        i += 1


# shifting seeds for each range
for i in range(len(SHIFT_LINES)):
    shiftSeeds(SHIFT_LINES[i][0], SHIFT_LINES[i][1])

# getting the lowest seed (will always be the start of the range)
lowest = float('inf')
for i in range(len(seeds)):
    if seeds[i][0] < lowest:
        lowest = seeds[i][0]

print(lowest)
