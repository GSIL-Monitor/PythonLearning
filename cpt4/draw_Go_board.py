import turtle

t = turtle.Pen()
my_color = ('green', 'red', 'yellow', 'black')
t.width(4)
t.speed(0.1)

x = -18 * 15
y = 18 * 15
for i in range(19):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x + 18 * 15 * 2, y)
    t.penup()
    t.goto(x + 18 * 15 * 2 + 5, y - 5)
    t.write(i + 1)
    y = y - 30

x = -18 * 15
y = 18 * 15
for i in range(19):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, y - 18 * 15 * 2)
    t.penup()
    t.goto(x - 5, y - 18 * 15 * 2 - 15)
    t.write(i + 1)
    x = x + 30

cx = cy = [-180, 0, 180]
for x in cx:
    for y in cy:
        t.penup()
        t.goto(x, y - 4)
        t.pendown()
        t.circle(4)

t.penup()
t.goto(500, 500)

turtle.done()
