import sys

N = int(sys.stdin.readline().rstrip().strip())

for i in range(N):
    string = sys.stdin.readline().strip()
    printString = string[0] + string[-1]
    print(printString)
