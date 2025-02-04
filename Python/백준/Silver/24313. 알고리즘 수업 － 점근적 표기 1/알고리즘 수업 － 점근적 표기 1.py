import sys

a1, a0 = map(int, sys.stdin.readline().rstrip().split(" "))
c = int(sys.stdin.readline().rstrip())
n0 = int(sys.stdin.readline().rstrip())

endN = 101

for i in range(n0, endN, 1):
    if (a1 * i) +a0 > c*i:
        print(0)
        break
    else:
        if i == endN-1:
            print(1)
    