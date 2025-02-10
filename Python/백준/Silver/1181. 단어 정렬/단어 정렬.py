import sys

n = int(sys.stdin.readline().rstrip())
wordList = []

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    if word not in wordList:
        wordList.append(word)
        
wordList.sort()
wordList.sort(key = lambda x: (len(x), x[0]))

print("\n".join(str(word)for word in wordList))