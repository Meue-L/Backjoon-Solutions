import sys

sqXList = []
sqYList = []

for _ in range(3):
    a, b = map(int, sys.stdin.readline().rstrip().split(" "))
    if a in sqXList:
        sqXList.pop(sqXList.index(a))
    else:
        sqXList.append(a)

    if b in sqYList:
        sqYList.pop(sqYList.index(b))
    else:
        sqYList.append(b)

print(sqXList[0], sqYList[0])
