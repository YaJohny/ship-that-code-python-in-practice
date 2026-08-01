set1 = set(input().split())
set2 = set(input().split())

interection = set1 & set2
sorted_list = sorted(interection)
display = " ".join(sorted)
print(display)