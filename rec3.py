import turtle

#t = turtle.Turtle()

t.speed(100)

t.pensize(2)
s = turtle.Screen()
s.bgcolor("black")

#t.color("red")
def draw(l, d):
    print("depth =", d, ", ", end="")
    if d == 0:
        t.circle(l/2)
        print("Terminated")
        return None
    for i in range(180):
        t.color("white") if i%3 else t.color("pink")
        #t.color("red")
        t.forward(3*i/5)
        #t.color("pink")
        t.circle(i*2, 60)
        t.forward(i/5)
        t.circle(i*2, 90)
        t.forward(i/5)
        t.circle(i*2, 120)


draw(200, 2)
turtle.done()
