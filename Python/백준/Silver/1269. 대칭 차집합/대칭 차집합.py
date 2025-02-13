import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))

AList = list(map(int, sys.stdin.readline().rstrip().split(" ")))
BList = list(map(int, sys.stdin.readline().rstrip().split(" ")))

ADict = dict.fromkeys(AList, 0)
BDict = dict.fromkeys(BList, 0)

AmB = []
for i in range(n):
    if AList[i] in BDict:
        pass
    else:
        AmB.append(AList[i])

BmA = []
for j in range(m):
    if BList[j] in ADict:
        pass
    else:
        BmA.append(BList[j])

DualList = list(set(AmB+BmA))

sys.stdout.write(str(len(DualList)))