import sys

k = int(sys.stdin.readline().rstrip())

for j in range(k):
    a, line = sys.stdin.readline().strip().split(" ")

    string = ""

    for i in range(len(line)):
        string += line[i] * int(a)

    print(string)
