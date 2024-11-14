FILE_NAME = 'day06.txt'

lines = open(FILE_NAME).readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

# getting times and distances
times = list(map(int, lines[0].split(':')[1].strip().split()))
distances = list(map(int, lines[1].split(':')[1].strip().split()))

total = 1  # result variable

# starting from zero
# stop when we reach the first time that satisfies the condition
# or when we pass time//2 (will not reach condition)
for i in range(0, len(times)):

    time = times[i]
    distance = distances[i]

    t = 0
    while t <= time//2:
        if t * (time-t) > distance:
            break

        t += 1

    # goto next iteration if we don't satisfy the condition
    else:
        continue

    # getting the amount of ways we satisfy the condition
    # and multiplying it to the total
    total *= (time - t - t + 1)

print(total)
