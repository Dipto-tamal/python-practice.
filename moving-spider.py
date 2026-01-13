import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Moving Colorful Spider")

spider = turtle.Turtle()
spider.shape("turtle")
spider.speed(0)
spider.width(3)
turtle.colormode(1)

# Random color
def random_color():
    return (random.random(), random.random(), random.random())

# Draw spider body
def draw_spider():
    spider.clear()

    # Body
    spider.color(random_color())
    spider.begin_fill()
    spider.circle(20)
    spider.end_fill()

    # Head
    spider.penup()
    spider.goto(spider.xcor(), spider.ycor() + 35)
    spider.pendown()
    spider.color(random_color())
    spider.begin_fill()
    spider.circle(12)
    spider.end_fill()

    spider.penup()
    spider.goto(spider.xcor(), spider.ycor() - 35)
    spider.pendown()

# Move spider
def move():
    draw_spider()
    spider.forward(10)

    if abs(spider.xcor()) > 300 or abs(spider.ycor()) > 250:
        spider.right(180)

    screen.ontimer(move, 100)

move()
turtle.done()
