import math
from turtle import *
import random

class Ball(Turtle):
    def __init__(self, radius, color, speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius=radius
        self.color(color)
        self.speed(speed)
        
def check_collision(Ball1, Ball2):
    if Ball1.radius+Ball2.radius>=math.sqrt(math.pow((Ball2.pos()-Ball1.pos(0)),2)+math.pow((Ball2.pos(1)-Ball1.pos(1)),2)):
            print("collision")
    else:
        print("no collision")
                                   
                                   
Ball1=Ball(300,"blue", 20)
Ball2=Ball(200, "pink", 10)

    

