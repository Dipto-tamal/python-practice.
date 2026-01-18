import turtle
import time
import math

# ---------------- Screen ----------------
screen = turtle.Screen()
screen.setup(1000, 650)
screen.title("Perfect Animated House 🏠")
screen.bgcolor("#87CEEB")  # sky

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# ---------------- Grass ----------------
pen.penup()
pen.goto(-500, -300)
pen.color("#2ecc71")
pen.begin_fill()
pen.pendown()
for _ in range(2):
    pen.forward(1000)
    pen.right(90)
    pen.forward(220)
    pen.right(90)
pen.end_fill()

# ---------------- Trees ----------------
def draw_tree(x):
    pen.penup()
    pen.goto(x, -300)
    pen.pendown()

    pen.color("saddlebrown")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(22)
        pen.left(90)
        pen.forward(70)
        pen.left(90)
    pen.end_fill()

    pen.penup()
    pen.goto(x - 35, -230)
    pen.color("darkgreen")
    pen.begin_fill()
    pen.circle(50)
    pen.end_fill()

for x in range(-450, 500, 150):
    draw_tree(x)

# ---------------- Sun ----------------
pen.penup()
pen.goto(350, 220)
pen.color("yellow")
pen.begin_fill()
pen.pendown()
pen.circle(45)
pen.end_fill()

# ---------------- House Body ----------------
pen.penup()
pen.goto(-200, -300)
pen.color("#f39c12")
pen.begin_fill()
pen.pendown()
for _ in range(2):
    pen.forward(400)
    pen.left(90)
    pen.forward(260)
    pen.left(90)
pen.end_fill()

# ---------------- Roof (Perfect) ----------------
pen.penup()
pen.goto(-220, -40)
pen.color("#8e44ad")
pen.begin_fill()
pen.pendown()
pen.forward(440)
pen.left(120)
pen.forward(260)
pen.left(120)
pen.forward(260)
pen.end_fill()

# ---------------- Windows ----------------
def window(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.color("lightblue")
    pen.begin_fill()
    pen.pendown()
    for _ in range(4):
        pen.forward(60)
        pen.left(90)
    pen.end_fill()

window(-140, -120)
window(80, -120)

# ---------------- Door (HINGE BASED) ----------------
door = turtle.Turtle()
door.speed(0)
door.color("saddlebrown")
door.width(2)

door.penup()
door.goto(-40, -300)  # hinge position
door.setheading(90)
door.pendown()

def draw_door(angle):
    door.clear()
    door.penup()
    door.goto(-40, -300)
    door.setheading(90 - angle)
    door.pendown()
    door.begin_fill()
    for _ in range(2):
        door.forward(140)
        door.right(90)
        door.forward(80)
        door.right(90)
    door.end_fill()

# closed door
draw_door(0)

# ---------------- Door Animation ----------------
for a in range(0, 70, 2):
    draw_door(a)
    time.sleep(0.04)

# ---------------- Text ----------------
pen.penup()
pen.goto(0, -330)
pen.color("black")
pen.write("Perfect Animated Python House 🏠",
          align="center", font=("Arial", 14, "bold"))

turtle.done()
