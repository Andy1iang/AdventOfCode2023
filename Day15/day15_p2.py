FILE_NAME = 'day15.txt'

lines = open(FILE_NAME).read()
words = lines.split(',')

# parallel arrays for boxes and the values in the boxes
boxes = [[] for _ in range(256)]
boxVals = [[] for _ in range(256)]

# function to get hash value


def hashValue(word):
    val = 0
    for c in word:
        val += ord(c)
        val *= 17
        val %= 256
    return val


for w in words:
    # if we are assigning
    if '=' in w:
        key = w.split('=')[0]
        val = w.split('=')[1]

        # finding index
        idx = -1
        try:
            idx = boxes[hashValue(key)].index(key)
        except:
            idx = -1

        # if we are adding
        if idx == -1:
            boxes[hashValue(key)].append(key)
            boxVals[hashValue(key)].append(val)

        # if we are editing
        else:
            boxVals[hashValue(key)][idx] = val

    # if we are deleting
    else:
        key = w[:len(w)-1:]
        idx = -1
        try:
            idx = boxes[hashValue(key)].index(key)
        except:
            idx = -1
        if idx != -1:
            boxes[hashValue(key)].pop(idx)
            boxVals[hashValue(key)].pop(idx)

# getting values from all boxes
total = 0
for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        val = 1
        val *= (1+i)
        val *= (1+j)
        val *= int(boxVals[i][j])
        total += val

print(total)
