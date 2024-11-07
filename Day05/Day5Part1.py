doc = open('Day5.txt', 'r').readlines()

allSeeds = doc[0][6::].strip().split()
allSeeds = list(map(int, allSeeds))


def shiftSeeds(seeds, start, end):
    ranges = []
    shifts = []

    for i in range(start, end):
        dest, source, interval = doc[i].split()
        different = int(dest)-int(source)

        ranges.append((int(source), int(source)+int(interval)-1))
        shifts.append(different)

    for i in range(len(seeds)):
        for j in range(len(ranges)):
            if seeds[i] >= ranges[j][0] and seeds[i] <= ranges[j][1]:
                seeds[i] += shifts[j]
                break

    return seeds


allSeeds = shiftSeeds(allSeeds, 3, 13)
allSeeds = shiftSeeds(allSeeds, 15, 24)
allSeeds = shiftSeeds(allSeeds, 26, 68)
allSeeds = shiftSeeds(allSeeds, 70, 114)
allSeeds = shiftSeeds(allSeeds, 116, 162)
allSeeds = shiftSeeds(allSeeds, 164, 191)
allSeeds = shiftSeeds(allSeeds, 193, 221)

print(min(allSeeds))
