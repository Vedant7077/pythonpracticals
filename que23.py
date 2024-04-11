rows = 4

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

# 1
# 12
# 123
# 1234

rows = 5
for i in range(1,rows+1):
    print(str(i)*i)

# 1
# 22
# 333
# 4444
# 55555