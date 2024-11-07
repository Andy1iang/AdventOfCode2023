FILE_NAME = 'day04.txt'

lines = open(FILE_NAME).readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

total = 0
for line in lines:
    wins = 0

    # making input
    winNums, nums = line.split('|')
    winNums = set(winNums.split(':')[1].strip().split())
    nums = nums.strip().split()

    # getting winning number counts for each line
    for n in nums:
        if n in winNums:
            wins += 1

    # getting winning value if more than one number match
    if wins > 0:
        total += 2**(wins-1)


print(total)
