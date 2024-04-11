filename  = input("Enter file name:")

with open(filename,'r') as file:
    content  = file.read()
    digit_count = sum(1 for char in content if char.isdigit())

print("Number of digits in file",digit_count)