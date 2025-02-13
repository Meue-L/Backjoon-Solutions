import sys

fullString = sys.stdin.readline().rstrip()

partDict = {}

for i in range(len(fullString)):
    for j in range(i, len(fullString)):
        if fullString[i:j+1] in partDict:
            partDict[fullString[i:j+1]] +=1
        else:
            partDict[fullString[i:j+1]] = 1


sys.stdout.write(str(len(list(partDict.keys()))))