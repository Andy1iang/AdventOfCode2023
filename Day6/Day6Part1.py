doc = open('Day6.txt', 'r').readlines()
times = doc[0].strip().split()[1:]
distances = doc[1].strip().split()[1:]

times = list(map(int,times))
distances = list(map(int,distances))

total = 1

for i in range(len(times)):
    
    subtotal = 0
    
    time = times[i]
    distance = distances[i]
    for j in range(time+1):
        traveled = (times[i]-j)*(j)
        if traveled > distance:
            subtotal += 1
            
    total *= subtotal
            
    

print(total)