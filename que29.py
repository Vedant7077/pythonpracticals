def is_palindrome(num):
    return str(num) == str(num)[::-1]
number = int(input("number:"))
if is_palindrome(number):
    print("it is palindeome")
else:
    print("it is not palindrome")