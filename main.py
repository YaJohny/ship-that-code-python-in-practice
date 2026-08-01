def is_palindrome(text):
    return text == text[::-1]

text = input()
if is_palindrome(text):
    print("yes")
else:
    print("no")
