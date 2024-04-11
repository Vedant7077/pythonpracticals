my_list = [1,2,3,4,5]
reverse = []
for i in range(len(my_list)-1,-1,-1):
    reverse.append(my_list[i])
print(reverse)