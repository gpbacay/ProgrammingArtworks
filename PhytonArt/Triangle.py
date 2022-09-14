import turtle
import colorsys as cs

p = turtle.Turtle()
p.screen.bgcolor('black')

p.penup()
p.goto(-200,-100)
p.pendown()
p.speed(10)

a = 400
h = 0
n = 100

def triangle():
    global a,n,h
    for i in range(40):
        c = cs.hsv_to_rgb(h,1,0.6)
        h=h+(1/n)
        p.color(c)
        p.forward(a)
        p.left(120)
        a=a-10
        
triangle()
triangle()

p.hideturtle()
turtle.done()

#Run Command: python Triangle.py
