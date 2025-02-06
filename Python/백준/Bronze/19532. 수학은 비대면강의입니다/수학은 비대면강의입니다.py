import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().rstrip().split(" "))
flag = 0

for i in range(-999, 1000, 1):
    for j in range(-999, 1000, 1):
        if (a*i)+(b*j) == c:
            if (d*i)+(e*j) == f:
                flag = 1
                break
    if flag == 1:
        break
    
print(i, j)