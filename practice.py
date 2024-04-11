with open('myfile.txt','r') as file:
    content = file.read()
    digits= sum(1 for char in content if char.isdigit())

print(digits)