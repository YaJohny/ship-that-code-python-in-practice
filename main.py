def min_max(numbers):
    return min(numbers), max(numbers)

n = int(input())
numbers = [int(input()) for x in range(n)]
min, max = min_max(numbers)

print(f"{min}\n{max}")







