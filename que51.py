class badPassowrdError(Exception):
    pass
passw = input("Enter passsword:")
if(len(passw)<8):
    raise badPassowrdError("Password sould be 8 characters long")
else:
    print("Valid Password")