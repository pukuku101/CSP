import turtle
cursor=turtle.Turtle("square")
colors=["white","black","red","blue","green","yellow"]
xrow=[]
yrow=[]
stampids=[0]
ins=0
colory=300
for i in range(6):
    colorturtle=turtle.Turtle("circle")
    color=colors.pop()
    colorturtle.fillcolor(color)
    colorturtle.pencolor(color)
    colorturtle.pu()
    colorturtle.speed(0)
    colorturtle.goto(-350,colory)
    colory=colory-30
colorturtle.pencolor("black")
for i in range(10):
    yrow.append(0)
for i in range(10):
    xrow.insert(ins,yrow[:])
    ins=ins+1

#############################initilization####################
###Drawing turtle
cursor.hideturtle()
cursor.speed(0)
cursor.pu()
cursor.goto(-300,-300)
cursor.pd()
cursor.shapesize(3)
for i in range(4):
    cursor.fd(600)
    cursor.lt(90)
for i in range(len(xrow)):
    cursor.left(90)
    cursor.fd(60)
    cursor.right(90)
    cursor.fd(600)
    cursor.backward(600)
for i in range(len(xrow)):
    cursor.fd(60)
    cursor.right(90)
    cursor.fd(600)
    cursor.backward(600)
    cursor.left(90)
cursor.pu()
###Save turtle

###################################Fuction definitions########################
def funcclick(x,y):
    if(abs(x)<=300 and abs(y)<=300):
        lcor=int((x+300)/60)
        x=(lcor*60)-270
        wcor=int((y+300)/60)
        y=(wcor*60)-270
        cursor.goto(x,y)
        tempobj=xrow.pop(lcor)
        rendundancy=tempobj.pop(wcor)
        cursor.clearstamp(rendundancy)
        id=cursor.stamp()
        stampids.append(id)
        tempobj.insert(wcor,id)
        xrow.insert(lcor,tempobj)
    elif (x<=-320):
        if (y>=286 and y<=310):
            cursor.pencolor("yellow")
            cursor.fillcolor("yellow")
        elif(y>=261 and y<=285):
            cursor.pencolor("green")
            cursor.fillcolor("green")
        elif(y>=230 and y<=250):
            cursor.pencolor("blue")
            cursor.fillcolor("blue")

def deletefunc():
    lateststamp=len(stampids)
    cursor.clearstamp(stampids[lateststamp-1])






wn=turtle.Screen()
wn.onclick(funcclick)
wn.onkeypress(deletefunc, key="z")
wn.listen()
wn.mainloop()
