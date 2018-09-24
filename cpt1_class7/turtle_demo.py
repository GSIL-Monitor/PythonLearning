import datetime
import turtle
#
# turtle.Turtle.showturtle()
# turtle.turtleTurtle.write('Kingddd')
# join 的效率比 + 的好

t = turtle.Pen()
my_color = ('green', 'red', 'yellow', 'black')
t.width(4)
t.speed(0.1)

for i in range(20):
    t.penup()
    t.goto(0, -i*10)
    t.pendown()
    t.color(my_color[i%len(my_color)])
    t.circle(10*i+10)
    t.color('black')
    t.write(i+1, font=("Arial", 12, "normal"))

turtle.done()
