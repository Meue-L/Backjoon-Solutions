import sys

wordList = []
verticalWord = ""

for i in range(5):
    wordList.append(list(sys.stdin.readline().rstrip()))

for i in range(15):
    for j in range(5):
        try:
            verticalWord += wordList[j][i]
        except:
            continue

print(verticalWord)
