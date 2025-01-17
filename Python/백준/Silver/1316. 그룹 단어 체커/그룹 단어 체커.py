import sys

N = int(sys.stdin.readline().rstrip())
CountOfGroupWords = N

for i in range(N):
    word = sys.stdin.readline().rstrip()
    spendLetter = []
    nowLetter = ""

    for j in range(len(word)):
        if word[j] in spendLetter:
            CountOfGroupWords -= 1
            break
        elif word[j] != nowLetter:
            spendLetter.append(nowLetter)
            nowLetter = word[j]
        else:
            continue

print(CountOfGroupWords)
