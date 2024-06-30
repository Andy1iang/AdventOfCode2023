f = open('Day4.txt', 'r')
doc = f.readlines()
total = 0


for line in doc:
    tempLine = line.split(':')[1].strip()
    winning = tempLine.split('|')[0].strip()
    winning = winning.split()
    nums = tempLine.split('|')[1].strip()
    nums = nums.split()
    
    winning = set(winning)
    nums = set(nums)
    
    points = 0
    
    if len(winning.intersection(nums)) > 0:
        points = 1
        for i in range(len(winning.intersection(nums))-1):
            points *= 2
            
    total += points
    
print(total)