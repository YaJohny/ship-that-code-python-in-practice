n = int(input())
nums = {name: int(grade) for _ in range(n) for name, grade in [input().split()]}
sorted_nums = sorted(nums, key=lambda x: nums[x], reverse=True)

for name in sorted_nums:
    print(name)
