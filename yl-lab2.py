import turtle
from turtle import *
import random
turtle.colormode(225)
class Square(Turtle):
      def __init__(self, size, shape, color):
        Turtle.__init__(self, shape)
        self.size(size)
        self.shape=shape
        self.color(color)

      def random_color(self):
          r = random.randint(0,256)
          g = random.randint(0,256)
          b = random.randint(0,256)
          self.color= color(r,g,b)
s=Square(10,"square","black")
s.random_color()
