FILE_NAME = 'day18.txt'

lines = [line.strip() for line in open(FILE_NAME).readlines()]

# same approach as part 1, but with different parsing

directions = {'3': (-1, 0), '1': (1, 0), '2': (0, -1), '0': (0, 1)}

points = [(0, 0)]

borders = 0

for line in lines:
    key = line.split()[2]
    steps, dir = key[2:7], key[7]
    steps = int(steps, 16)
    borders += steps
    deltaRow, deltaCol = directions[dir]
    deltaRow, deltaCol = deltaRow * steps, deltaCol * steps
    points.append((points[-1][0] + deltaRow, points[-1][1] + deltaCol))

area = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) %
           len(points)][1]) for i in range(len(points)))) // 2
insideArea = area - (borders // 2) + 1

print(insideArea+borders)
