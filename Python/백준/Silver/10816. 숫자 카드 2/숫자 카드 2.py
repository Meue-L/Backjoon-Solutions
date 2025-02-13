import sys

n = int(sys.stdin.readline().rstrip())

hands = list(map(int, sys.stdin.readline().rstrip().split(" ")))

m = int(sys.stdin.readline().rstrip())

fields = list(map(int,sys.stdin.readline().rstrip().split(" ")))
fieldsDict = dict.fromkeys(fields, 0)

for i in range(n):
    if hands[i] in fieldsDict:
        fieldsDict[hands[i]] += 1
        
countList =[]
for j in range(m):
    if fields[j] in fieldsDict:
        countList.append(fieldsDict[fields[j]])
        
sys.stdout.write(" ".join(str(count) for count in countList))