import turtle
colors=["red","green","blue","pink","yellow","purple"]
turtle.speed(0)
for i in range(600):
    turtle.pencolor(colors[i%6])
    turtle.fd(200)
    turtle.right(45)
    turtle.fd(100)
    turtle.right(90)
    turtle.fd(50)
    turtle.home()
    turtle.right(i)




##import turtle
##for i in range(500):
##    turtle.forward(200)
##    turtle.right(72)
##    turtle.forward(100)
##    turtle.right(90)
##    turtle.forward(20)
##    turtle.right(1)
##turtle.mainloop()
