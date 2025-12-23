
def all_eq(lst):
    max_len = 0
    for s in lst:
        if len(s) > max_len:
            max_len = len(s)
    result = []
    for s in lst:
        result.append(s + "_" * (max_len - len(s)))   
    return result

n = int(input("Num of strings: "))
lst = []
for i in range(n):
    lst.append(input())

print(all_eq(lst))

