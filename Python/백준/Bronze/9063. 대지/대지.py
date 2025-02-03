import sys

n = int(sys.stdin.readline().rstrip())

xList = []
yList = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split(" "))
    xList.append(a)
    yList.append(b)

print((max(xList) - min(xList)) * (max(yList) - min(yList)))
