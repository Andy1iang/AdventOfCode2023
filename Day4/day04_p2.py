FILE_NAME = 'day04.txt'

lines = open(FILE_NAME).readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

total = 0

# array to keep track of how many we have of each ticket
multi = [1]*(len(lines))

for i in range(len(lines)):
    wins = 0
    winNums, nums = lines[i].split('|')
    winNums = set(winNums.split(':')[1].strip().split())
    nums = nums.strip().split()

    # getting wins
    for n in nums:
        if n in winNums:
            wins += 1

    # duplicating tickets 
    for j in range(wins):
        multi[i+j+1] += 1*multi[i] # multiplied by how many we have of the current one


print(sum(multi))
