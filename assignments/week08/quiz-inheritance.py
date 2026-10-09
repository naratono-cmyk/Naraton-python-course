""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""


class Rectangle:
    def __init__(self, width, length):
        self.__width = width
        self.__length = length

    def getArea(self):
        return f"Area of {self.__length} length and {self.__width} width : {self.__length * self.__width}"

    def getPerimeter(self):
        return f"Perimeter of {self.__length} length and {self.__width} width : {(self.__length + self.__width) * 2}"

    def isSquare(self):
        return self.__length == self.__width

myrectangle = Rectangle(5, 10)

print(myrectangle.getArea())
print(myrectangle.getPerimeter())
print(myrectangle.isSquare())