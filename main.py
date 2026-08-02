try:
    a = int(input())
    b = float(input())
    div = round(a/b, 2)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("invalid input")
else:
    print(div)