data = input("Enter data:")
with open("myfile.txt","w") as file:
    file.write(data)
print("Data has been written to file")