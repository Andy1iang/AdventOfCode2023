FILE_NAME = 'day09.txt'

lines = open(FILE_NAME).readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

total = 0

# for each line
for line in lines:

    # getting the differences
    # storing them in a 2d array
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

    # adding the last element of each row
    for num in nums:
        total += num[-1]

print(total)
