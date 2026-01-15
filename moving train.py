import turtle
import math
import time
import random

# ---------------- SCREEN ----------------
screen = turtle.Screen()
screen.setup(1200, 650)
screen.title("Advanced Zigzag Train 🚆 with Smoke")
screen.bgcolor("#87CEEB")

# ---------------- PEN ----------------
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# ---------------- GROUND ----------------
pen.penup()
pen.goto(-600, -300)
pen.color("#2ecc71")
pen.begin_fill()
pen.pendown()
for _ in range(2):
    pen.forward(1200)
    pen.right(90)
    pen.forward(220)
    pen.right(90)
pen.end_fill()

# ---------------- TREES ----------------
def draw_tree(x):
    pen.penup()
    pen.goto(x, -300)
    pen.pendown()

    pen.color("saddlebrown")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(22)
        pen.left(90)
        pen.forward(65)
        pen.left(90)
    pen.end_fill()

    pen.penup()
    pen.goto(x - 35, -235)
    pen.color("darkgreen")
    pen.begin_fill()
    pen.circle(50)
    pen.end_fill()

for x in range(-550, 600, 140):
    draw_tree(x)

# ---------------- RAILWAY ----------------
rail = turtle.Turtle()
rail.hideturtle()
rail.speed(0)
rail.color("black")
rail.width(4)

rail_points = []

x = -600
while x <= 600:
    y = -100 + 28 * math.sin(x * 0.04)
    rail_points.append((x, y))
    x += 6

# draw two rails
for offset in [-8, 8]:
    rail.penup()
    rail.goto(rail_points[0][0], rail_points[0][1] + offset)
    rail.pendown()
    for px, py in rail_points:
        rail.goto(px, py + offset)

# sleepers
rail.width(2)
for px, py in rail_points[::10]:
    rail.penup()
    rail.goto(px - 12, py - 10)
    rail.pendown()
    rail.forward(24)

# ---------------- TRAIN ----------------
train = turtle.Turtle()
train.hideturtle()
train.speed(0)

# ---------------- SMOKE ----------------
smoke = turtle.Turtle()
smoke.hideturtle()
smoke.speed(0)

smokes = []

def draw_smoke(x, y):
    smokes.append([x, y, 12])

def update_smoke():
    smoke.clear()
    for s in smokes[:]:
        s[1] += 2
        s[2] += 0.3
        smoke.penup()
        smoke.goto(s[0], s[1])
        smoke.color("gray")
        smoke.begin_fill()
        smoke.circle(s[2])
        smoke.end_fill()
        if s[2] > 30:
            smokes.remove(s)

def draw_train(x, y):
    train.clear()
    train.penup()
    train.goto(x, y)
    train.pendown()

    # engine
    train.color("red")
    train.begin_fill()
    for _ in range(2):
        train.forward(110)
        train.left(90)
        train.forward(55)
        train.left(90)
    train.end_fill()

    # chimney
    train.penup()
    train.goto(x + 20, y + 55)
    train.pendown()
    train.color("black")
    train.begin_fill()
    for _ in range(2):
        train.forward(18)
        train.left(90)
        train.forward(28)
        train.left(90)
    train.end_fill()

    draw_smoke(x + 30, y + 85)

    # coach
    train.penup()
    train.goto(x + 120, y)
    train.pendown()
    train.color("blue")
    train.begin_fill()
    for _ in range(2):
        train.forward(130)
        train.left(90)
        train.forward(55)
        train.left(90)
    train.end_fill()

    # wheels
    for wx in [x + 25, x + 80, x + 150, x + 210]:
        train.penup()
        train.goto(wx, y - 12)
        train.pendown()
        train.color("black")
        train.begin_fill()
        train.circle(11)
        train.end_fill()

# ---------------- ANIMATION ----------------
i = 0
while True:
    x, y = rail_points[i]
    draw_train(x - 60, y + 15)
    update_smoke()

    i += 1
    if i >= len(rail_points):
        i = 0

    time.sleep(0.03)





