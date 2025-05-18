import turtle

screen = turtle.Screen()
screen.bgcolor('blue')
all_turtles = []

def s():
    t = turtle.Turtle()
    t.shape('turtle')
    t.color('green')
    t.speed(1)
    t.penup()
    t.goto(0, 0)
    all_turtles.append(t)

def f(x, y):
    if len(all_turtles) > 0:
        prev_turtle = all_turtles[-1]
        prev_turtle.goto(x, y)
    s()

s()
screen.onscreenclick(f)
screen.mainloop()