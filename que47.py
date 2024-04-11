import math

def volume(shape,*args):
    if shape == 'cube':
        side  = args[0]
        return side ** 3
    elif shape == 'cuboid':
        leng,bred,hei= args
        return leng*bred*hei
    elif shape  == 'cylinder':
        radius,hieght = args
        return math.pi*(radius**2)*hieght
    
print("Volume of cube (side 4):", volume("cube", 4))
print("Volume of cuboid (3x4x5):", volume("cuboid", 3, 4, 5))
print("Volume of cylinder (radius 2, height 6):", volume("cylinder", 2, 6))
