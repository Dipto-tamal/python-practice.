import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")

spider = turtle.Turtle()
spider.speed(0)
spider.color("white")
spider.width(2)

# Draw spider body
spider.penup()
spider.goto(0, -20)
spider.pendown()
spider.begin_fill()
spider.circle(40)
spider.end_fill()

spider.penup()
spider.goto(0, 40)
spider.pendown()
spider.begin_fill()
spider.circle(25)
spider.end_fill()

# Draw legs
spider.penup()
spider.goto(0, 20)
spider.setheading(0)

for i in range(8):
    spider.penup()
    spider.goto(0, 20)
    spider.pendown()
    spider.setheading(45 * i)
    spider.forward(80)
    spider.backward(20)
    spider.right(30)
    spider.forward(40)

# Eyes
spider.penup()
spider.goto(-10, 70)
spider.dot(5, "red")
spider.goto(10, 70)
spider.dot(5, "red")

spider.hideturtle()
turtle.done()
