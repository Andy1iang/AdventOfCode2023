FILE_NAME = 'day09.txt'

lines = open(FILE_NAME).readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

total = 0

# same approach as part 1 with minor tweak in addition
for line in lines:
    nums = []
    nums.append(list(map(int, line.split())))
    while True:
        temp = []
        zeros = True
        for i in range(len(nums[-1])-1):
            n = nums[-1][i+1]-nums[-1][i]
            temp.append(n)
            if n != 0:
                zeros = False
        if zeros:
            break
        nums.append(temp)
        diff = nums[-1][-1] - nums[-1][-2]

    # add every other number at the start
    # subtract every other number after that
    for i in range(len(nums)):
        if i%2 == 0:
            total += nums[i][0]
        else:
            total -= nums[i][0]

print(total)
