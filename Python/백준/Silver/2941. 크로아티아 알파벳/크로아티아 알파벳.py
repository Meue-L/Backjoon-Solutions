import sys

word = sys.stdin.readline().rstrip()
count = len(word)

for i in range(1, len(word)):
    if word[i] == "=":
        if word[i - 1] in "cs":
            count -= 1
        elif word[i - 1] == "z":
            if i - 2 >= 0 and word[i - 2] == "d":
                count -= 1
            count -= 1
    elif word[i] == "-":
        if word[i - 1] in "cd":
            count -= 1
    elif i != 0 and word[i] == "j":
        if word[i - 1] in "ln":
            count -= 1


print(count)
