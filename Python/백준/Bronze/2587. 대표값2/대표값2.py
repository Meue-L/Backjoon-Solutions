import sys

numList = []

for _ in range(5):
    numList.append(int(sys.stdin.readline().rstrip()))
    
print(int(sum(numList) / 5))
print(sorted(numList)[2])