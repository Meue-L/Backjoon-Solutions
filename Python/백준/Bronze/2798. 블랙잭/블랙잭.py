import sys

a, b = map(int, sys.stdin.readline().rstrip().split(" "))

cardList = list(map(int, sys.stdin.readline().rstrip().split(" ")))
total = 0
result = 0

for i in range(0, len(cardList) - 2):
    for j in range(i+1, len(cardList) - 1):
        for k in range(j+1, len(cardList)):
            total = cardList[i] + cardList[j] + cardList[k]
            if total > result and total <= b:
                result = total
            

print(result)