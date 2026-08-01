def avarage(*args):
    args_sum = sum(args)
    return args_sum / len(args)

n = int(input())
nums = [float(input()) for _ in range(n)]
print(avarage(*nums))