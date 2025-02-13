import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))

S = []
checkList = []

for i in range(n):
    S.append(sys.stdin.readline().rstrip())
    
SDict = dict(zip(S, range(n)))
count = 0

for j in range(m):
    if sys.stdin.readline().rstrip() in SDict:
        count+=1
        

print(count)
    
    
