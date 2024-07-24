from turtle import*
import math

title("Girasol")
bgcolor('black')

fillcolor('green')
begin_fill()
pencolor('black')
forward(7)
right(90)
forward(300)
right(90)
forward(15)
right(90)
forward(300)
right(90)
end_fill()

speed(0)
fillcolor('brown')
s = 137.508 *(math.pi / 180.0)
for i in range (160 + 40):
    r = 4 * math.sqrt(i)
    f = i * s
    o = r * math.cos(f)
    p = r * math.sin(f)
    penup()
    goto(o,p)
    setheading(i * 137.508)
    pendown()
    if i < 160:
        stamp()
    else:
        fillcolor('yellow')
        begin_fill()
        right(20)
        forward(46)
        left(40)
        forward(70)
        left(140)
        forward(70)
        left(40)
        forward(70)
        end_fill()
        hideturtle()
mainloop()

