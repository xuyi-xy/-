import turtle as t
t.pensize(4)
t.bgcolor("black")
t.speed(100)

sides = 6
colors = ["red", "blue", "orange", "green", "purple", "yellow"]
for x in range(300):
    t.pencolor(colors[x%sides])
    t.forward(x * 2/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)
