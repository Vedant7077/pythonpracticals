def is_armstrong(num):
    num_str = str(num)
    power = len(num_str)
    sum_of_digit = 0

    for digit_char in num_str:
        digit = int(digit_char)
        sum_of_digit+=digit ** power
    return sum_of_digit == num

number = int(input("Enter number:"))
if is_armstrong(number):
    print(number, "is armstrong")
else:
    print(number, "is not armstrong")