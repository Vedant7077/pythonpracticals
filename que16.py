numbers = [1,4,6,8,9,10]
prime = []

for num in numbers:
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            prime.append(num)
if prime:
    print("Prime Numbers:",prime)
else:
    print("no prime numbers found")
