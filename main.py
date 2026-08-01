set1 = input().split()
set2 = input().split()

interection = set1 and set2
sorted = list(interection).sort(reverse=True)
display = " ".join(sorted)