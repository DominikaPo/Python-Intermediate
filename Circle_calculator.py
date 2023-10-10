#Write a Python program to create a class representing a Circle. 
#Include methods to calculate its area and perimeter

class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        y = 3.14*self.r**2
        print("Area: ", y)
    def perimeter(self):
        z = 2*3.24*self.r
        print("Perimeter: ", z)

x = Circle(float(input()))
x.area()
x.perimeter()
