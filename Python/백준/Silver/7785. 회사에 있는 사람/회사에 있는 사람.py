import sys

n = int(sys.stdin.readline().rstrip())

onWorkingDict = {}

for i in range(n):
    workerLog, logType = map(str, sys.stdin.readline().rstrip().split(" "))
    if workerLog in onWorkingDict:
        if logType == "leave":
            onWorkingDict.pop(workerLog)
    else:
        if logType == "enter":
            onWorkingDict[workerLog] = logType

onWorkingList = list(onWorkingDict.keys())
onWorkingList.sort(reverse = True, key = lambda x : (x))

sys.stdout.write("\n".join(worker for worker in onWorkingList))