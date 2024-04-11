def avg(*args):
    return sum(args)/len(args)

def add(*args):
    return sum(args)

def square(num):
    return num**2

def cube(num):
    return num**3

def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)