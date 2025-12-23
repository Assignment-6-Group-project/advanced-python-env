from collections import Counter

items = input().split()
freq = Counter(items)
most_popular = max(freq, key=freq.get)
purchased_once = [item for item, count in freq.items() if count == 1]
sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

print("Purchase frequency:")
for item, count in freq.items():
    print(f"{item}: {count}")

print(f"\nMost popular item: {most_popular}")

print("\nPurchased once:", " ".join(purchased_once))

print("\nSorted by frequency:")
for item, count in sorted_items:
    print(f"{item} {count}")
























































