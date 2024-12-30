text = input("Enter a string: ")

# Check for palindrome
if text == text[::-1]:
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")
