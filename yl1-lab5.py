from turtle import *
import random

class Square(Turtle):
    def __init__(self, size):
        Turtle.__init__(self)
        self.size = size
        self.shape("square")
        self.shapesize(size*size)
   

    def Area(self):
        return self.side*self.side

    def random_color(self):
        r = random.random()
        g = random.random()
        b = random.random()
        self.color(r,g,b)

Square1= Square(5)
Square1.random_color()


        


        
