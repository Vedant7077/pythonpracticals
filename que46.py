def area(lenght,width=None):
    if width is None:
        return lenght**2
    else:
        return lenght*width
print("Area of square:",area(5))
print("Area of Rectangle:",area(5,10))