n = int(input())
numbers = [int(input()) for i in range(n)]
doubled_evens = [print(2*x) for x in numbers if x % 2 == 0]
