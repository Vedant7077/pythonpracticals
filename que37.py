
tuple_elements = tuple(input("Enter elements separated by spaces: ").split())

total_sum = 0
for item in tuple_elements:
    for char in item:
        if char.isdigit():
            total_sum += int(char)

print("Sum of digits:", total_sum)
