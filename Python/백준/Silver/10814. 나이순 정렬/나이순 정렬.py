import sys

n = int(sys.stdin.readline().rstrip())
memberList = []

for i in range(n):
    memberList.append(list(map(str, sys.stdin.readline().rstrip().split(" "))))

memberList.sort(key= lambda x: (int(x[0])))

for j in range(len(memberList)):
    print(memberList[j][0], memberList[j][1])