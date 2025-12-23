a = input("Input: ")
b = input("Input: ")

shifts = set()
for i in range (len(b)):
    shift = b[i:] + b[:i]
    shifts.add(shift)
print(shifts)

count = 0
blength = len(b)

for i in range(len(a)-blength+1):
    substring = a[i:i+blength]
    if substring in shifts:
        count += 1
print(count)