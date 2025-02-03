import sys

while True:
    nList = []

    n = int(sys.stdin.readline().rstrip())
    if n == -1:
        break

    for i in range(n-1):
        if n % (i + 1) == 0:
            nList.append(i + 1)

    if sum(nList) == n:
        print(f"{n} = {" + ".join(str(number) for number in nList)}")
    else:
        print(f"{n} is NOT perfect.")