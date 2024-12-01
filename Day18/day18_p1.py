FILE_NAME = 'day18.txt'

lines = [line.strip() for line in open(FILE_NAME).readlines()]

# up, down, left, right
directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

# keeping track of the points that we land on
points = [(0, 0)]

# keeping track of how many border tiles there are
borders = 0

# for each line in the input
# we get the direction and the number of steps, then move there
# we also keep track of the borders number
for line in lines:
    dir, steps, _ = line.split()
    borders += int(steps)
    deltaRow, deltaCol = directions[dir]
    deltaRow, deltaCol = deltaRow * int(steps), deltaCol * int(steps)
    points.append((points[-1][0] + deltaRow, points[-1][1] + deltaCol))

# we find the total area of the polygon
# via shoelace formula and Pick's theorem

# A = 1/2 * sum(x[i] * (y[i-1] - y[i+1]))
area = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) %
           len(points)][1]) for i in range(len(points)))) // 2

# Inside Area = Area - (borders / 2) + 1
insideArea = area - (borders // 2) + 1

# print the result
print(insideArea+borders)
