FILE_NAME = 'day06.txt'

lines = open(FILE_NAME).readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

# getting times and distances
time = int(lines[0].split(':')[1].replace(' ',''))
distance = int(lines[1].split(':')[1].replace(' ',''))

# starting from zero
# stop when we reach the first time that satisfies the condition
# or when we pass time//2 (will not reach condition)
t = 0
while t <= time//2:
    if t * (time-t) > distance:
        break

    t += 1

# getting the amount of ways we satisfy the condition
print(time - t - t + 1)
