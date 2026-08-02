n = int(input())
nums = {name: grade for _ in range(n) for name, grade in [input().split()]}
nums.sort(key=lambda x: x["grade"])

for name in nums.keys:
    print(name)
