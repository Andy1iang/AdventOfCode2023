doc = open('Day5.txt', 'r').readlines()

allSeeds = doc[0][6::].strip().split()
allSeeds = list(map(int, allSeeds))

tempSeedNums = []  # ranges of all seeds to use
for i in range(0, len(allSeeds), 2):
    tempSeedNums.append([allSeeds[i], allSeeds[i]+allSeeds[i+1]-1])


def shiftSeeds(seed, start, end):
    ranges = []
    shifts = []

    for i in range(start, end):
        source, dest, interval = doc[i].split()
        different = int(dest)-int(source)

        ranges.append((int(source), int(source)+int(interval)-1))
        shifts.append(different)

    for j in range(len(ranges)):
        if seed >= ranges[j][0] and seed <= ranges[j][1]:
            seed += shifts[j]
            break

    return seed


i = 0
k = 0
while True:
    i = shiftSeeds(i, 193, 221)
    i = shiftSeeds(i, 164, 191)
    i = shiftSeeds(i, 116, 162)
    i = shiftSeeds(i, 70, 114)
    i = shiftSeeds(i, 26, 68)
    i = shiftSeeds(i, 15, 24)
    i = shiftSeeds(i, 3, 13)

    for seedRange in tempSeedNums:
        if i >= seedRange[0] and i <= seedRange[1]:
            print(k)
            exit()

    k += 1
    i = k
