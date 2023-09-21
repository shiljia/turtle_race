
import turtle
import random
import time

a=turtle.Turtle()
b=turtle.Turtle()
t=turtle.Turtle()
t.speed(0)

s=turtle.Screen()
s.bgcolor('black')

a.shape('turtle')
a.color('blue')
b.shape('turtle')
b.color('red')

t.pu()
t.goto(0,250)
t.pd()
t.color('red')
t.write('TURTLE RACE',align='center',font=('arial',35,'bold'))
t.fd(180)
t.bk(360)

t.pu()
t.goto(-300,150)
t.pd()

t.fillcolor('green')
t.begin_fill()
t.fd(600)
t.rt(90)
t.fd(300)
t.rt(90)
t.fd(600)
t.rt(90)
t.fd(300)
t.end_fill()

t.pu()
t.goto(250,125)
t.pd()
t.rt(180)

t.pensize(8)
for i in range(25):
    if(i%2==0):
        c='black'
    else:
        c='white'
    t.color(c)
    t.fd(10)

a.goto(-250,75)
b.goto(-250,-75)

a.speed(8)
b.speed(8)
a.pu()
b.pu()

while True:
    a.fd(random.randrange(1,15))
    b.fd(random.randrange(1,15))
    time.sleep(0.1)
    if(a.pos()[0]>=250):
        w='A'
        break
    if(b.pos()[0]>=250):
        w='B'
        break

t.color('lime')
t.pu()
t.goto(0,-250)
t.pd()

r=('THE WINNER IS '+w)

t.write(r,align='center',font=('arial',20,'bold'))


        

