import sys

n = int(sys.stdin.readline().rstrip())
nList = [0]*10001

for _ in range(n):
    nList[int(sys.stdin.readline().rstrip())] += 1
    
for i in range(1, 10001):
    if nList[i] != 0:
        for _ in range(nList[i]):
            print(i)