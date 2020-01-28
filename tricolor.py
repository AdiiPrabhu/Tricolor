# Python script to create Indian flag using turtle.
import turtle
import time
screen = turtle.getscreen()
screen.bgcolor("#b3daff")
screen.title("Indian Flag - Aditya(@team_quantico)")
adi = turtle.Turtle()
adi.speed(100)
adi.penup()
adi.shape("turtle")

flag_height = 300
flag_width = 450

start_x = -225
start_y = 150

ht = flag_height/3
width = flag_width

radius = ht / 2


def recy(x, y, height, width, color):
    adi.goto(x,y)
    adi.pendown()
    adi.color(color)
    adi.begin_fill()
    adi.forward(width)
    adi.right(90)
    adi.forward(height)
    adi.right(90)
    adi.forward(width)
    adi.right(90)
    adi.forward(height)
    adi.right(90)
    adi.end_fill()
    adi.penup()


def stripes():
    x = start_x
    y = start_y
    recy(x, y, ht, width, "#FF9933")
    y = y - ht   
    recy(x, y, ht, width, "white")
    y = y - ht               

    recy(x, y, ht, width, '#138808')
    y = y - ht


def chakra():
    adi.speed(1)
    adi.goto(0,0)
    color = "#000080"
    adi.penup()
    adi.color(color)
    adi.fillcolor(color)
    adi.goto(0, 0 - radius)
    adi.pendown()
    adi.circle(radius)

    for _ in range(24):
        adi.penup()
        adi.goto(0,0)
        adi.left(15)
        adi.pendown()
        adi.forward(radius)
  
    

time.sleep(0)
stripes()
chakra()
adi.hideturtle()
screen.mainloop()
