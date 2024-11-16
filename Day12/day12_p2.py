FILE_NAME = 'day12.txt'

lines = open(FILE_NAME).readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

# same approach as part 1, but with a cache to store results
# so that we don't have to recompute the same subproblems
cache = {}

def permutations(springs, nums):
    if springs == '':
        return 1 if len(nums) == 0 else 0

    if len(nums) == 0:
        return 1 if "#" not in springs else 0
    
    if (springs, tuple(nums)) in cache:
        return cache[(springs, tuple(nums))]

    cnt = 0

    if springs[0] in ".?":
        cnt += permutations(springs[1:], nums)

    if springs[0] in "#?":
        if (nums[0] <= len(springs)) and ('.' not in springs[:nums[0]:]) and (nums[0] == len(springs) or springs[nums[0]] != "#"):
            cnt += permutations(springs[(nums[0]+1):], nums[1:])

    cache[((springs, tuple(nums)))] = cnt
    return cnt


total = 0
for line in lines:
    springs, nums = line.split()
    nums = list(map(int, nums.split(',')))

    # repeat the input 5 times
    springs = '?'.join([springs]*5)
    nums *= 5

    total += permutations(springs, nums)

print(total)
