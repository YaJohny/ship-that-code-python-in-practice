words = input().split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

for x, y in counts.items:
    print(f"{x} {y}")