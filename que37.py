
n = int(input("Enter number of elements:"))
t = tuple(int(input(f"Enter elemnt {i+1} :"))for i in range(0,n))
print(t)
print(f"Sum: {sum(t)}")
