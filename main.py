def is_palindrome(text):
    text_list = list(text)
    reversed_text = text_list[::-1]
    return text_list == reversed_text


text = input()
if is_palindrome(text):
    print("yes")
else:
    print("no")
