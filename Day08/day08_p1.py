FILE_NAME = 'day08.txt'

lines = open(FILE_NAME).readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

directions = lines[0]

# Create a dictionary of nodes
# key: node name; value: tuple of left and right nodes
nodes = {}
for line in lines[2::]:
    nodes[line[0:3:]] = (line[7:10:], line[12:15:])

total = 0
curr = 'AAA'
end = 'ZZZ'

# traverse while we are not at ZZZ node
while curr != end:
    # if the direction is left, go to the left node, else go to the right node
    if directions[total % len(directions)] == 'L':
        curr = nodes[curr][0]
    else:
        curr = nodes[curr][1]

    total += 1

print(total)
