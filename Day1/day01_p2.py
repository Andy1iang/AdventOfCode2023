FILE_NAME = 'day01.txt'

lines = open(FILE_NAME).readlines()

# Map to convert words to numbers
nums = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

total = 0
for line in lines:

    # same approach as part 1 with edits
    temp = ''

    for i in range(len(line)):
        if line[i].isnumeric(): # if character is number
            temp += line[i]
            break

        # if character is in bounds and next characters make up a word
        elif i < len(line)-3 and line[i:i+3] in nums:
            temp += str(nums[line[i:i+3]])
            break
        elif i < len(line)-4 and line[i:i+4] in nums:
            temp += str(nums[line[i:i+4]])
            break
        elif i < len(line)-5 and line[i:i+5] in nums:
            temp += str(nums[line[i:i+5]])
            break
    
    # same approach but in reverse
    for i in range(len(line)-1, -1, -1):
        if line[i].isnumeric():
            temp += line[i]
            break
        elif i < len(line)-3 and line[i:i+3] in nums:
            temp += str(nums[line[i:i+3]])
            break
        elif i < len(line)-4 and line[i:i+4] in nums:
            temp += str(nums[line[i:i+4]])
            break
        elif i < len(line)-5 and line[i:i+5] in nums:
            temp += str(nums[line[i:i+5]])
            break

    total += int(temp)

print(total)