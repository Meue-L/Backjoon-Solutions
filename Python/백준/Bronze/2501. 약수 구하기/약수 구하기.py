import sys
n, k = map(int, sys.stdin.readline().rstrip().rsplit())
nList = []

for i in range(n):
    if n%(i+1) == 0:
        nList.append(i+1)
    else:
        continue
if len(nList) < k:
    print(0)
else:
    print(nList[k-1])