import sys
angleList = []

for _ in range(3):
    angleList.append(int(sys.stdin.readline().rstrip()))

if sum(angleList) != 180:
    print("Error")
else:
    if angleList.count(60) == 3:
        print("Equilateral")
    elif angleList.count(angleList[0])==2 or angleList.count(angleList[1]) == 2:
        print("Isosceles")
    else:
        print("Scalene")