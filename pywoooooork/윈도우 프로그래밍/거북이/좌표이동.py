import turtle as t
import time # sleep()
import random as r


#좌표 이동 - turtle.goto(x,y)



t.shape("turtle")
t.speed(0)
# t.goto(200,0)



t.goto(0,0)

n = 200000000
for i in range(n):
    x = r.randint(0, 360)
    y = r.randint(0, 100)
    t.setheading(x)
    t.forward(y)
    if t.ycor == 400:
        t.goto(0,0)
    elif t.ycor == -400:
        t.goto(0,0)

    elif t.xcor == 400:
        t.goto(0,0)

    elif t.xcor == -400:
        t.goto(0,0)







t.mainloop()