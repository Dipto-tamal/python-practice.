import turtle

screen = turtle.Screen()
screen.setup(900, 500)
screen.bgcolor("#87CEEB")   # sky blue
screen.title("Beautiful Moving Car")

car = turtle.Turtle()
car.speed(0)
car.hideturtle()
car.penup()

# Draw road
road = turtle.Turtle()
road.hideturtle()
road.penup()
road.goto(-450, -150)
road.color("gray")
road.begin_fill()
road.forward(900)
road.right(90)
road.forward(120)
road.right(90)
road.forward(900)
road.right(90)
road.forward(120)
road.end_fill()

# Car drawing function
def draw_car(x, y):
    car.clear()

    # Car body
    car.goto(x, y)
    car.color("red")
    car.begin_fill()
    car.forward(200)
    car.left(90)
    car.forward(50)
    car.left(90)
    car.forward(200)
    car.left(90)
    car.forward(50)
    car.end_fill()

    # Car top
    car.goto(x + 40, y + 50)
    car.color("darkred")
    car.begin_fill()
    car.forward(120)
    car.left(90)
    car.forward(50)
    car.left(90)
    car.forward(120)
    car.left(90)
    car.forward(50)
    car.end_fill()

    # Windows
    car.color("lightblue")
    car.goto(x + 55, y + 60)
    car.begin_fill()
    car.forward(40)
    car.left(90)
    car.forward(30)
    car.left(90)
    car.forward(40)
    car.left(90)
    car.forward(30)
    car.end_fill()

    car.goto(x + 115, y + 60)
    car.begin_fill()
    car.forward(40)
    car.left(90)
    car.forward(30)
    car.left(90)
    car.forward(40)
    car.left(90)
    car.forward(30)
    car.end_fill()

    # Wheels
    car.color("black")
    car.goto(x + 40, y - 10)
    car.begin_fill()
    car.circle(20)
    car.end_fill()

    car.goto(x + 140, y - 10)
    car.begin_fill()
    car.circle(20)
    car.end_fill()

# Move car
x = -400
y = -120

def move():
    global x
    draw_car(x, y)
    x += 5
    if x > 450:
        x = -450
    screen.ontimer(move, 50)

move()
turtle.done()

