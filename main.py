def is_palindrome(text):
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]


text = input()
if is_palindrome(text):
    print("yes")
else:
    print("no")
