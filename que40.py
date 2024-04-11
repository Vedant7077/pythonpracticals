import re
password = input("Enter password:")
if len(password)<8:
    print("password should be minimum 8 characters long")
elif not re.search("[a-z]",password):
    print("password must include lowercase letter")
elif not re.search("[A-Z]",password):
    print("password must include uppercase letter")
elif not re.search("[!@#$%^&*()]",password):
    print("password must include special characters")
else:
    print("Valid Password")