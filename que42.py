import math_functions as m

numbers = [1,2,4,5,6,7]

print("Average:",m.avg(*numbers))
print("Add : ",m.add(*numbers))
print("Square: ",m.square(2))
print("Cube:",m.cube(3))
print("Factorial:",m.factorial(5))



import calendar
year = int(input("year:"))
month = int(input("Month:"))
# print(calendar.calendar(year))
print(calendar.month(year,month))