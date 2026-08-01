set1 = set(input().split())
set2 = set(input().split())

intersection = set1 & set2
sorted_list = sorted(intersection)
display = " ".join(sorted_list)
print(display)