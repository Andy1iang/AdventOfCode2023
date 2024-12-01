from heapq import heappush, heappop

FILE_NAME = 'day17.txt'

grid = [list(map(int, line.strip())) for line in open('day17.txt')]

# same approach as part 1 with a slight modification
# in the requirements for the streak to be >= 4 and < 10 in some cases

seen = set()

# (loss, row, col, deltaRow, deltaCol, streak)
pq = [(0, 0, 0, 0, 0, 0)]

while pq:
    loss, row, col, deltaRow, deltaCol, streak = heappop(pq)

    if row == len(grid)-1 and col == len(grid[0])-1 and streak >= 4:
        print(loss)
        break

    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
        continue

    if (row, col, deltaRow, deltaCol, streak) in seen:
        continue

    seen.add((row, col, deltaRow, deltaCol, streak))

    if streak < 10 and (deltaRow, deltaCol) != (0, 0):
        newRow = row + deltaRow
        newCol = col + deltaCol
        if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]):
            heappush(pq, (loss +
                     grid[newRow][newCol], newRow, newCol, deltaRow, deltaCol, streak+1))

    if streak >= 4 or (deltaRow, deltaCol) == (0, 0):
        for rowMove, colMove in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (rowMove, colMove) != (deltaRow, deltaCol) and (rowMove, colMove) != (-deltaRow, -deltaCol):
                newRow = row + rowMove
                newCol = col + colMove
                if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]):
                    heappush(pq, (loss + grid[newRow][newCol],
                                  newRow, newCol, rowMove, colMove, 1))
