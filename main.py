n = int(input())
nums = {name: int(grade) for _ in range(n) for name, grade in [input().split()]}
sorted_nums = sorted(nums, key=lambda x: x[name], reverse=True)

for name in sorted_nums:
    print(name)
