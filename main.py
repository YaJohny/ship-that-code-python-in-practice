n = int(input())
nums = [int(input()) for _ in range(n)]
a = list(set(nums))
a.sort(reverse=True)
print(a[1])
