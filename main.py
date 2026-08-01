def avarage(*args):
    args_sum = sum(args)
    return round((args_sum / len(args)), 2)

n = int(input())
nums = [float(input()) for _ in range(n)]
print(avarage(*nums))