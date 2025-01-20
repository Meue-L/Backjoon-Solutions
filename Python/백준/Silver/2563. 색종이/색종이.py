import sys

page = [[0] * 100 for _ in range(100)]
papers = int(sys.stdin.readline().rstrip())

for i in range(papers):
    x, y = map(int, sys.stdin.readline().rstrip().split(" "))

    for j in range(x, x + 10):
        for k in range(y, y + 10):
            page[k][j] = 1

count = 0

for l in range(len(page)):
    count += page[l].count(1)

print(count)
