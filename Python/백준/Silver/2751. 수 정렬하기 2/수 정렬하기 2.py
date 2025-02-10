import sys

n = int(sys.stdin.readline().rstrip())

nList = []

for _ in range(n):
    nList.append(int(sys.stdin.readline().rstrip()))
    
sortedNList = sorted(nList)
    
for i in range(n):
    print(sortedNList[i])