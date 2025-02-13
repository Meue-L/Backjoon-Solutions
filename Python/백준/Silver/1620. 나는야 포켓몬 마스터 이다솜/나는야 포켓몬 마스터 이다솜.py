import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))

poketmonDict = {}

for i in range(n):
    poketmonDict[sys.stdin.readline().rstrip()] = str(i+1)
reversedPoketmonDict = dict(map(reversed, poketmonDict.items()))

for j in range(m):
    question = sys.stdin.readline().rstrip()
    
    if question in poketmonDict:
        sys.stdout.write(poketmonDict[question]+ "\n")
    else:
        sys.stdout.write(reversedPoketmonDict[question]+ "\n")