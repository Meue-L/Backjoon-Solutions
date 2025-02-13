import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))

neverHeardNameList = []
neverSeenNameList = []

for i in range(n):
    neverHeardNameList.append(sys.stdin.readline().rstrip())
    
neverHeardNameDict = dict.fromkeys(neverHeardNameList, 0)

neverSeenAndHeardNameList = []

for j in range(m):
    neverHeardName = sys.stdin.readline().rstrip()
    
    if neverHeardName in neverHeardNameDict:
        neverSeenAndHeardNameList.append(neverHeardName)
        
neverSeenAndHeardNameList.sort(key=lambda x : x)
sys.stdout.write(str(len(neverSeenAndHeardNameList))+"\n")
sys.stdout.write("\n".join(name for name in neverSeenAndHeardNameList))