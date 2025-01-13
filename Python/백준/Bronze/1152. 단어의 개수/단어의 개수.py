import sys

line = sys.stdin.readline().strip().split(" ")

if line[0] == "":
    print(0)
else:
    print(len(line))
