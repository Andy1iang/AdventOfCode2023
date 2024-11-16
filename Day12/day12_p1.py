FILE_NAME = 'day12.txt'

lines = open(FILE_NAME).readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

# recursive function to find all possible permutations of the springs
def permutations(springs, nums):

    # base cases
    # return 1 if base case valid or 0 if not
    if springs == '':
        return 1 if len(nums) == 0 else 0

    if len(nums) == 0:
        return 1 if "#" not in springs else 0

    # recursive cases
    cnt = 0

    # if the current spring is a '.' or '?', goto the next
    if springs[0] in ".?":
        cnt += permutations(springs[1:], nums)

    # if the current could be a broken spring that matches
    if springs[0] in "#?":
        # conditions: enough springs left, no '.' in the next nums[0] springs, and the next spring is not a '#' after the nums[0] springs
        if (nums[0] <= len(springs)) and ('.' not in springs[:nums[0]:]) and (nums[0] == len(springs) or springs[nums[0]] != "#"):
            # goto the next spring after the nums[0] springs
            cnt += permutations(springs[(nums[0]+1):], nums[1:])

    return cnt


# find the total number of permutations for all the lines
total = 0
for line in lines:
    springs, nums = line.split()
    nums = list(map(int, nums.split(',')))
    total += permutations(springs, nums)

print(total)
