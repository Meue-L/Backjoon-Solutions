import sys

board = []

maxX, maxY, maxValue = -1, -1, -1

for i in range(9):
    board.append(sys.stdin.readline().rstrip().split(" "))
    tempMaxValue = max(board[i])

    if maxValue < int(tempMaxValue):
        maxValue = int(tempMaxValue)
        maxX = i + 1
        maxY = board[i].index(tempMaxValue) + 1

print(maxValue)
print(maxX, maxY)
