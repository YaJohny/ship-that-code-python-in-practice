def validate_age(years):
    if years < 0:
        raise ValueError("age must be non-negative")
    elif years > 150:
        raise ValueError("age too large")
    else:
        return years

years = int(input())
try:
    validate_age(years)
except ValueError as e:
    print(f"{years} {e}")
else:
    print(f"{years} ok")
