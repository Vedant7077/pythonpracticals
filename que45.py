def greet(name = None, mssg = None):
    if name and mssg:
        print(f"hello {name},{mssg}")
    elif name:
        print("Hello",name)
    else:
        print("hello")
greet()
greet('Alice')
greet('alice','how are you?')