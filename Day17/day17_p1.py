from heapq import heappush, heappop

FILE_NAME = 'day17.txt'

grid = [list(map(int, line.strip())) for line in open('day17.txt')]

# Dijkstra's algorithm from top left corner to bottom right corner

# to keep track if we've visited a cell with the same state
seen = set()

# priority queue
# (loss, row, col, deltaRow, deltaCol, streak)
pq = [(0, 0, 0, 0, 0, 0)]

while pq:
    # pop the cell with the least heat loss
    loss, row, col, deltaRow, deltaCol, streak = heappop(pq)

    # if we've reached the bottom right corner
    if row == len(grid)-1 and col == len(grid[0])-1:
        print(loss)
        break

    # if we're out of bounds
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
        continue

    # if we've visited a cell with the same state
    if (row, col, deltaRow, deltaCol, streak) in seen:
        continue

    # mark the cell as visited
    seen.add((row, col, deltaRow, deltaCol, streak))

    # if we can continue in the same direction and we're not at the start
    if streak < 3 and (deltaRow, deltaCol) != (0, 0):
        newRow = row + deltaRow
        newCol = col + deltaCol
        if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]):
            heappush(pq, (loss +
                     grid[newRow][newCol], newRow, newCol, deltaRow, deltaCol, streak+1))

    # the directions we can turn to
    for rowMove, colMove in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if (rowMove, colMove) != (deltaRow, deltaCol) and (rowMove, colMove) != (-deltaRow, -deltaCol):
            newRow = row + rowMove
            newCol = col + colMove
            if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]):
                heappush(pq, (loss + grid[newRow][newCol],
                         newRow, newCol, rowMove, colMove, 1))
