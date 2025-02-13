import sys

n = int(sys.stdin.readline().rstrip())

deckList = list(map(int, sys.stdin.readline().rstrip().split(" ")))
deckDict = dict(zip(deckList, range(n)))

m = int(sys.stdin.readline().rstrip())

fieldList = list(map(int, sys.stdin.readline().rstrip().split(" ")))

onHisHandChecker = []

for i in range(m):
    if fieldList[i] in deckDict:
        onHisHandChecker.append(1)        
    else:
        onHisHandChecker.append(0)


sys.stdout.write(" ".join(str(flag) for flag in onHisHandChecker))