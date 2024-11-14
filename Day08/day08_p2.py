from math import lcm
# brute force takes too long
# so we need to find the least common multiple of the cycle lengths of each node
# lcm is when they will reach Z node at the same time

FILE_NAME = 'day08.txt'

lines = open(FILE_NAME).readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

directions = lines[0]

nodes = {}
for line in lines[2::]:
    nodes[line[0:3:]] = (line[7:10:], line[12:15:])

# function to get the length of path from A to Z for a given node


def getPath(node):
    cnt = 0
    while node[2] != 'Z':
        if directions[cnt % len(directions)] == 'L':
            node = nodes[node][0]
        else:
            node = nodes[node][1]
        cnt += 1

    return cnt


# count of all the path
pathCounts = []
for node in nodes:
    if node[2] == 'A':
        pathCounts.append(getPath(node))

# returning the lcm
# *pathCounts is used to unpack the list
print(lcm(*pathCounts))
