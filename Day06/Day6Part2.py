doc = open('Day6.txt', 'r').readlines()
time = int(''.join(doc[0].strip().split()[1:]))
distance = int(''.join(doc[1].strip().split()[1:]))

total = 0


for i in range(time+1):
    traveled = (time-i)*(i)
    if traveled > distance:
        total += 1
            
print(total)