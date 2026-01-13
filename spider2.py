import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Spider")

spider = turtle.Turtle()
spider.speed(0)
spider.width(3)

# Random color function
def random_color():
    return (random.random(), random.random(), random.random())

turtle.colormode(1)

# Body
spider.color(random_color())
spider.penup()
spider.goto(0, -20)
spider.pendown()
spider.begin_fill()
spider.circle(40)
spider.end_fill()

# Head
spider.color(random_color())
spider.penup()
spider.goto(0, 40)
spider.pendown()
spider.begin_fill()
spider.circle(25)
spider.end_fill()

# Eyes
spider.penup()
spider.goto(-10, 70)
spider.pendown()
spider.dot(8, "white")

spider.penup()
spider.goto(10, 70)
spider.pendown()
spider.dot(8, "white")

# Legs
def draw_leg(x, y, angle):
    spider.color(random_color())
    spider.penup()
    spider.goto(x, y)
    spider.setheading(angle)
    spider.pendown()
    spider.forward(60)
    spider.right(30)
    spider.forward(40)

# Left legs
draw_leg(-30, 20, 160)
draw_leg(-35, 0, 180)
draw_leg(-30, -20, 200)
draw_leg(-20, -40, 220)

# Right legs
draw_leg(30, 20, 20)
draw_leg(35, 0, 0)
draw_leg(30, -20, -20)
draw_leg(20, -40, -40)

spider.hideturtle()
turtle.done()
