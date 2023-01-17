import turtle as trtl
import random as rand
pen=trtl.Turtle()
length=30
wallnum=20
pen.speed(0)
pencolor="red"
x=0
y=0
runner=trtl.Turtle(shape="turtle")
runner.pu()
runner.goto(10,15)
wn=trtl.Screen()
runner.pd()
runner.pencolor(pencolor)
increase=30


def penmove():
    global length,y
    """length=length+15"""
    intdiv=rand.randint(31,length-60)
    randoor=length-intdiv
    intsub=rand.randint(0,intdiv-30)
    pen.fd(randoor)
    if (y<=15):
        pen.up()
        pen.fd(20)
        pen.down()
    else:
        pen.fd(20)
    pen.fd(intsub)
    pen.lt(90)
    pen.fd(30)
    pen.bk(30)
    pen.rt(90)
    pen.fd(intdiv-intsub)
    pen.lt(90)
    y=y+1
for i in range(0,wallnum):
    x=x+1
    pen.fd(length)
    pen.lt(90)
    length=length+increase
    if(x==4):
        penmove()
        x=3

pen.hideturtle()
def down():
    runner.setheading(270)
    move_runner()
def up():
    runner.setheading(90)
    move_runner()
def right():
    runner.setheading(0)
    move_runner()
def left():
    runner.setheading(180)
    move_runner()
def move_runner():
    runner.fd(20)

wn.onkeypress(down,"Down")
wn.onkeypress(up,"Up")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")
wn.onkeypress(move_runner,"g")
wn.listen()
wn.mainloop()
