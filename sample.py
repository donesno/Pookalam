import turtle
from math import sqrt
from turtle import *

#bg
t = turtle.Turtle()
bgcolor("antiquewhite")
t.pu()
t.setpos(-130,-300)
t.pd()
style = ('Verdana',20,)
t.write('     POOKALAM     ',font = style)
t.pu()


#layer1
t.speed("fastest")
t.color("white","pink")
t.setpos(00,-250)
t.pd()
t.pensize(5)
t.color("darkgreen","pink")
t.begin_fill()
t.circle(300)
t.end_fill()

#layer2

t.pu()
t.setpos(00,50)
t.pd()

t.color("orange","orange")
num_sides = 4
side_length = 208
angle = 360.0 / num_sides
 
for i in range(36):
    t.begin_fill()
    for i in range(num_sides):
        t.forward(side_length)
        t.right(angle)
    t.end_fill()
    t.right(70)


#layer3

t.pu()
t.setpos(00,50)
t.pd()

t.color("yellow","yellow")
num_sides = 4
side_length = 180
angle = 360.0 / num_sides
 
for i in range(36):
    t.begin_fill()
    for i in range(num_sides):
        t.forward(side_length)
        t.right(angle)
    t.end_fill()
    t.right(70)

#layer4

t.pu()
t.setpos(00,50)
t.pd()

t.color("white","white")
num_sides = 4
side_length = 140
angle = 360.0 / num_sides
 
for i in range(36):
    t.begin_fill()
    for i in range(num_sides):
        t.forward(side_length)
        t.right(angle)
    t.end_fill()
    t.right(70)

colors = ['darkred', 'red', 'orange', ]
#layer4.2

t.pu()
t.setpos(00,50)
t.pd()

#t.color("orange","white")
num_sides = 4
side_length = 120
angle = 360.0 / num_sides
 
for i in range(36):
    t.color(colors[i%3])
    t.begin_fill()
    for i in range(num_sides):
        t.forward(side_length)
        t.right(angle)
    t.end_fill()
 
    t.right(50)

#layer5
t.setpos(00,-71)
t.color("darkviolet","yellow")
t.begin_fill()
t.circle(120)
t.end_fill()

#layer6

t.pu()
t.setpos(00,50)
t.pd()

t.color("red","red")
num_sides = 4
side_length = 80
angle = 360.0 / num_sides
 
for i in range(36):
    t.begin_fill()
    for i in range(num_sides):
        t.forward(side_length)
        t.right(angle)
    t.end_fill()
    t.right(70)

#layer7

t.pu()
t.setpos(00,50)
t.pd()

t.color("darkviolet","darkviolet")
num_sides = 4
side_length = 70
angle = 360.0 / num_sides
 
for i in range(36):
    t.begin_fill()
    for i in range(num_sides):
        t.forward(side_length)
        t.right(angle)
    t.end_fill()
    t.right(70)

t.pensize(1)

#layer8
t.setpos(00,00)
t.color("darkgreen","darkgreen")
t.begin_fill()
t.circle(50)
t.end_fill()

#layer9

t.pu()
t.setpos(00,50)
t.pd()

t.color("orange","orange")
num_sides = 4
side_length = 30
angle = 360.0 / num_sides
 
for i in range(36):
    t.begin_fill()
    for i in range(num_sides):
        t.forward(side_length)
        t.right(angle)
    t.end_fill()
    t.right(70)

#layer10

t.pu()
t.setpos(00,50)
t.pd()

t.color("white","white")
num_sides = 4
side_length = 20
angle = 360.0 / num_sides
 
for i in range(10):
    t.begin_fill()
    for i in range(num_sides):
        t.forward(side_length)
        t.right(angle)
    t.end_fill()
    t.right(70)

#layer11
t.setpos(00,45)
t.color("darkviolet")
t.begin_fill()
t.circle(5)
t.end_fill()

t.hideturtle()
done()
