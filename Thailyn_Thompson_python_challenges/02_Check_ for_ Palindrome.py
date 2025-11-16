def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]
print(is_palindrome("racecar"))  # Output: True 
print(is_palindrome("A man a plan a canal Panama"))  # Output: True
print(is_palindrome("hello"))  # Output: False  