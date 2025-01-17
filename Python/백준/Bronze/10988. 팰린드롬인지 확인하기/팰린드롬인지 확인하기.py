import sys

word = sys.stdin.readline().rstrip()
reversedWord = word[::-1]

if word == reversedWord:
    print("1")
else:
    print("0")
