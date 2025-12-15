num = (input("Enter 6-digit num: "))
first3 = num[:3]
last3 = num[3:]
firstsum = sum(map(int, first3))
lastsum = sum(map(int, last3))
if firstsum == lastsum:
    print("YES")
else:
    print("NO")