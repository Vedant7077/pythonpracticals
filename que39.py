
string = input("Enter a string: ")

upper_count = sum(1 for char in string if char.isupper())
lower_count = sum(1 for char in string if char.islower())
digit_count = sum(1 for char in string if char.isdigit())

print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)
print("Number of digits:", digit_count)
