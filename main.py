def avarage(*args):
    sum = sum(args)
    return sum / len(args)

n = int(input())
nums = [float(input()) for _ in range(n)]
print(avarage(*nums))