import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))

board = []
for z in range(n):
    board.append(sys.stdin.readline().rstrip())

boardType = "W"
anotherBoardType = "B"
minCount = 64

for i in range(0, n-7):
    for j in range(0, m-7):
        count = 0
        anotherCount = 0
        
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x-i)%2 == 0:
                    if (y-j)%2 == 0:
                        if boardType != board[x][y]:
                            count +=1
                    else:
                        if boardType == board[x][y]:
                            count +=1
                else:
                    if (y-j)%2 == 0:
                        if boardType == board[x][y]:
                            count +=1
                    else:
                        if boardType != board[x][y]:
                            count +=1
                            
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x-i)%2 == 0:
                    if (y-j)%2 == 0:
                        if anotherBoardType != board[x][y]:
                            anotherCount +=1
                    else:
                        if anotherBoardType == board[x][y]:
                            anotherCount +=1
                else:
                    if (y-j)%2 == 0:
                        if anotherBoardType == board[x][y]:
                            anotherCount +=1
                    else:
                        if anotherBoardType != board[x][y]:
                            anotherCount +=1
                            
        if minCount > count:
            minCount = count
        if minCount > anotherCount:
            minCount = anotherCount

print(minCount)
        