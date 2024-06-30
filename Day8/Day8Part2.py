from math import lcm

doc = open('Day8.txt','r').read().splitlines()

directions = doc[0]
directionsLen = len(directions)
navigation = {}

for i in range(2,len(doc)):
    navigation[doc[i][0:3]] = (doc[i][7:10],doc[i][12:15])
    
allCounts = []
    
for line in doc[2::]:
    
    if line[2] == 'A':
    
        current = line[0:3]
        count = 0

        while current[2] != 'Z':
            
            if directions[count%directionsLen] == 'L':
                current = navigation[current][0]
            elif directions[count%directionsLen] == 'R':
                current = navigation[current][1]
                
            count += 1
    
        allCounts.append(count)
        
    
print(lcm(*allCounts))
    
     