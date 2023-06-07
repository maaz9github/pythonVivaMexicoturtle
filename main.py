# Maaztermin9  -turtle code meant to resemble the Mexican flag minimalist shield.  feel free to change things around.
import turtle

window = turtle.Screen()
window.title("Mexican Flag")
window.bgcolor("black")

flag = turtle.Turtle()
flag.speed(2)

green = "#138808"
white = "#FFFFFF"
red = "#CE1126"

flag.color(green)
flag.begin_fill()
flag.goto(-150, 200)
flag.goto(-150, -200)
flag.goto(150, -200)
flag.goto(150, 200)
flag.goto(-150, 200)
flag.end_fill()

flag.color(white)
flag.begin_fill()
flag.goto(-50, 200)
flag.goto(-50, -200)
flag.goto(50, -200)
flag.goto(50, 200)
flag.goto(-50, 200)
flag.end_fill()

flag.color(red)
flag.begin_fill()
flag.goto(50, 200)
flag.goto(50, -200)
flag.goto(150, -200)
flag.goto(150, 200)
flag.goto(50, 200)
flag.end_fill()

flag.penup()
flag.goto(0, 0)
flag.pendown()

flag.color("black")
flag.width(3)

flag.left(90)
flag.forward(10)
flag.right(90)
flag.circle(50, 360)
flag.left(180)
flag.right(90)
flag.forward(40)
flag.right(90)
flag.circle(20, 180)
flag.right(90)
flag.forward(20)

flag.left(45)
flag.forward(15)
flag.left(45)
flag.forward(40)
flag.left(90)
flag.forward(40)
flag.left(45)
flag.forward(20)

flag.left(90)
flag.forward(40)
flag.right(135)
flag.forward(50)
flag.right(90)
flag.forward(40)
flag.right(135)
flag.forward(50)
flag.right(90)
flag.forward(20)
flag.right(90)
flag.forward(69)
flag.left(100)
flag.forward(50)
flag.right(15)
flag.forward(5)

flag.penup()
flag.goto(-0, -0)
flag.pendown()
flag.color("#689F38")  # Dark green

flag.left(90)
flag.right(80)
flag.forward(10)
flag.left(90)
flag.forward(30)
flag.right(90)
flag.forward(10)
flag.right(90)
flag.forward(30)
flag.left(90)
flag.forward(20)
flag.right(90)
flag.forward(10)
flag.right(90)
flag.forward(20)
flag.left(90)
flag.forward(10)
flag.right(90)
flag.forward(15)
flag.right(90)
flag.forward(15)
flag.left(90)
flag.forward(15)
flag.right(90)
flag.forward(15)
flag.right(90)
flag.forward(15)
flag.left(90)
flag.forward(10)
flag.right(90)
flag.forward(20)
flag.right(90)
flag.forward(10)
flag.left(90)
flag.forward(30)
flag.right(90)
flag.forward(10)
flag.right(90)
flag.forward(30)
flag.left(90)
flag.forward(80)


flag.penup()
flag.goto(-2, -5)
flag.pendown()

flag.left(300)
flag.right(280)
flag.forward(10)
flag.left(90)
flag.forward(30)
flag.right(90)
flag.forward(10)
flag.right(90)
flag.forward(30)
flag.left(90)
flag.forward(20)
flag.right(90)
flag.forward(10)
flag.right(90)
flag.forward(20)
flag.left(90)
flag.forward(10)
flag.right(90)
flag.forward(15)
flag.right(90)
flag.forward(15)
flag.left(90)
flag.forward(15)
flag.right(90)
flag.forward(15)
flag.right(90)
flag.forward(15)
flag.left(90)
flag.forward(10)
flag.right(90)
flag.forward(20)
flag.right(90)
flag.forward(10)
flag.left(90)
flag.forward(30)
flag.right(90)
flag.forward(10)
flag.right(90)
flag.forward(30)
flag.left(90)
flag.forward(10)

#

flag.penup()
flag.goto(-20, -20)
flag.pendown()

flag.color("green")
flag.width(3)

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(1)  # speed of text

start_x = -124
start_y = -120
t.penup()
t.goto(start_x, start_y)
t.pendown()

# font TOP
font_style = ("Arial", 50, "bold")

letters = ["M", "E", "X", "I", "C", "O"]
letter_spacing = 50  # spacing
for letter in letters:
    t.write(letter, align="center", font=font_style)
    t.forward(letter_spacing)
#

t = turtle.Turtle()
t.speed(3)  # speed

start_x = -122
start_y = -124
t.penup()
t.goto(start_x, start_y)
t.pendown()

# font Bottom
font_style = ("Arial", 49, "bold")

def draw_outline(letter):
    t.penup()
    t.setheading(0)
    t.pendown()
    t.pensize(3)
    t.color("green")
    t.write(letter, align="center", font=font_style)
    t.penup()
    t.color("green")
    t.pendown()
    t.write(letter, align="center", font=font_style)

letters = ["M", "E", "X", "I", "C", "O"]
letter_spacing = 50
for letter in letters:
    t.write(letter, align="center", font=font_style)
    t.forward(letter_spacing)


flag.hideturtle()

turtle.done()

#Thank you [E\>Maaztermin9</3]
