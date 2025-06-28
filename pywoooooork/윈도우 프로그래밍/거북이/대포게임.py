import turtle as t
import random as r


def turn_up():
    t.left(2)

def turn_down():
    t.right(2)    


target = r.randint(50, 150)


def fire():
    ang = t.heading()
    while t.ycor() > 0:
        t.forward(15)
        t.right(5)
    d = t.distance(target, 0)
    t.right(d)

    if d < 25:
        t.color('blue')
        t.write("good", False, 'CENTER', ('',15))
    else:
        t.color('red')
        t.write("bad", False, 'center', ('', 15))
        t.color('black')
        t.goto(-200,10)
        t.setheading(ang)
    




t.goto(-300,0)
t. goto(300,0)

target = r.randint(50, 150)
t.color('green')
t.pensize(3)
t.up()
t.goto(target-25, 1)
t.down()
t.goto(target+25, 1)

t.color('black')
t.up()
t.goto(-200,10)
t.setheading(40)




t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")
t.listen()

t.mainloop()