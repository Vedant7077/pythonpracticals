#For sum of digits
n = int(input("number:"))
tot = 0
while(n>0):
    dig = n%10
    tot+=dig
    n//=10
print("Sum:",tot)


#For product of digits
n = int(input("numner:"))
tot = 1
while(n>0):
    dig = n%10
    tot*=dig
    n//=10
print("Sum:",tot)