import math

class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height= height
    def Area(self):
        return self.width * self.height
    def perimeter(self):
        return (self.width + self.height) * 2
    def hype(self):
        return math.sqrt(self.width**2 + self.height**2)


rect=Rectangle(50, 50)

print(rect.Area())
print(rect.hype())


class Person():
    def __init__(self, name, age, city, gender):
        self.name= name
        self.age= age
        self.city= city
        self.gender= gender
    def Breakfast(self, food):
        print(self.name+ "is eating" + food)

person1=Person(Dima, 16, Nazareth, Other)        
        
