s1 = input().strip()
s2 = input().strip()
if len(s1) != len(s2):
    print("NO")
else:
    freq = [0] * 26

    for c in s1:
        freq[ord(c) - ord('A')] += 1

    for c in s2:
        freq[ord(c) - ord('A')] -= 1

    if all(x == 0 for x in freq):
        print("YES")
    else:
        print("NO")