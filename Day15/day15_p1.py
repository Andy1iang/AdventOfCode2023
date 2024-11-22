FILE_NAME = 'day15.txt'

lines = open(FILE_NAME).read()
words = lines.split(',')

# getting hash values from words according to instructions
total = 0
for w in words:
    val = 0
    for c in w:
        val += ord(c)
        val *= 17
        val %= 256
    total += val

print(total)
