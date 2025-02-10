import sys

n = int(sys.stdin.readline().rstrip())

numList = []

for _ in range(n):
    numList.append(int(sys.stdin.readline().rstrip()))
    
sortedNumList = sorted(numList)

for i in range(n):
    print(sortedNumList[i])