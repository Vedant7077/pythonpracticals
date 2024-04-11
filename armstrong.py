num = int(input("Enter number:"))
sum =0
for x in str(num):
    sum+=int(x)**(len(str(num)))
print(sum)
if sum==num:
    print("It is armstrong")
else:
    print("Not")