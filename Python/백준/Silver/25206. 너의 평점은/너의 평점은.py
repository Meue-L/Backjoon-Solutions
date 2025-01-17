import sys

totalScore = 0
lectureCount = 0

while True:
    try:
        inputList = sys.stdin.readline().rstrip().split(" ")
        if inputList == [""]:
            raise EOFError

        if inputList[2] == "P":
            continue
        else:
            if inputList[2] == "A+":
                totalScore += 4.5 * float(inputList[1])
                lectureCount += float(inputList[1])
            if inputList[2] == "A0":
                totalScore += 4.0 * float(inputList[1])
                lectureCount += float(inputList[1])
            if inputList[2] == "B+":
                totalScore += 3.5 * float(inputList[1])
                lectureCount += float(inputList[1])
            if inputList[2] == "B0":
                totalScore += 3.0 * float(inputList[1])
                lectureCount += float(inputList[1])
            if inputList[2] == "C+":
                totalScore += 2.5 * float(inputList[1])
                lectureCount += float(inputList[1])
            if inputList[2] == "C0":
                totalScore += 2.0 * float(inputList[1])
                lectureCount += float(inputList[1])
            if inputList[2] == "D+":
                totalScore += 1.5 * float(inputList[1])
                lectureCount += float(inputList[1])
            if inputList[2] == "D0":
                totalScore += 1.0 * float(inputList[1])
                lectureCount += float(inputList[1])
            if inputList[2] == "F":
                totalScore += 0.0 * float(inputList[1])
                lectureCount += float(inputList[1])

    except EOFError:
        break

print(totalScore / lectureCount)
