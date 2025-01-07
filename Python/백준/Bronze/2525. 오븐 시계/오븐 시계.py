h, m = map(int, input().split(" "))
minuteGap = int(input())
hourGap = 0


if minuteGap > 59:
    hourGap = minuteGap // 60
    minuteGap -= 60 * hourGap

h += hourGap
m += minuteGap

if m > 59:
    m -= 60
    h += 1
if h > 23:
    h -= 24


print(f"{h} {m}")
