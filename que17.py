import random

n = int(input("Enter the number of elements: "))
random_list = [random.randint(1, 100) for _ in range(n)]
print("Random List:", random_list)
