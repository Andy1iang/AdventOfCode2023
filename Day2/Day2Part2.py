max = {'red':0, 'green':0, 'blue':0}

f = open('Day2.txt', 'r')
doc = f.readlines()

total = 0

for line in doc:
    max['red'] = 0
    max['green'] = 0
    max['blue'] = 0
    
    trials = line.split(':')[1]
    
    for case in trials.split(';'):
        for pull in case.split(','):
            pull = pull.strip()
            if max[pull.split(' ')[1]] < int(pull.split(' ')[0]):
                max[pull.split(' ')[1]] = int(pull.split(' ')[0])
    
    total += max['red'] * max['green'] * max['blue']
        
print(total)
