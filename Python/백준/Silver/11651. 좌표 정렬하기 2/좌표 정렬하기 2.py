import sys

n = int(sys.stdin.readline().rstrip())

spotList = []

for _ in range(n):
    spotList.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))
    
spotList.sort(key = lambda x: (x[1], x[0]))

print("\n".join(str(" ".join(str(location) for location in spot)) for spot in spotList))