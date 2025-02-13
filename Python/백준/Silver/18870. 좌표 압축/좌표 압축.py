import sys

n = int(sys.stdin.readline().rstrip())

spotList = list(map(int, sys.stdin.readline().rstrip().split(" ")))

sortedSpotList = sorted(list(set(spotList)))
indexDict = dict(zip(sortedSpotList, range(len(sortedSpotList))))
    
for i in range(n):
    spotList[i]=indexDict[spotList[i]]
    
sys.stdout.write(" ".join(str(spot)for spot in spotList))