
def is_prime(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                return False
        return True
    return False

try:
    number = int(input("Enter number:"))
    if is_prime(number):
        print("number is prime")
    else:
        print("not prime")
except ValueError:
    print("Only numbers are allowed")