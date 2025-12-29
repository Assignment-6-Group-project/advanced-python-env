#1
n = int(input("Enter n: "))

for num in range(1, n + 1):
    digits = str(num)
    valid = True

    for d in digits:
        if d == '0' or num % int(d) != 0:
            valid = False
            break

    if valid:
        print(num, end=" ")


#2
def swap(arr):
    arr[0], arr[-1] = arr[-1], arr[0]

m = int(input("Enter array length: "))
A = []

for i in range(m):
    A.append(int(input()))

print("Original array:", A)

swap(A)

print("Modified array:", A)















