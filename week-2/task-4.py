n, m = map(int, input().split())
text = input()
words = set()  
for i in range(n - m + 1):
    word = text[i:i + m]  
    words.add(word)

print(len(words))

















