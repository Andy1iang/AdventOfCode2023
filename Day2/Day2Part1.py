limits = {'red':12, 'green':13, 'blue':14}

f = open('Day2.txt', 'r')
doc = f.readlines()

total = 0

for line in doc:
    ID = int(line.split(':')[0].split(' ')[1])
    trials = line.split(':')[1]
    add = True
    
    for case in trials.split(';'):
        for pull in case.split(','):
            pull = pull.strip()
            if limits[pull.split(' ')[1]] < int(pull.split(' ')[0]):
                add = False
    
    if add is True:
        total += ID
        
print(total)
