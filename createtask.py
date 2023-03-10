import turtle
cursor=turtle.Turtle("square")
xrow=[]
yrow=[]
stampids=[0]
ins=0
for i in range(10):
    yrow.append(0)
for i in range(10):
    xrow.insert(ins,yrow[:])
    ins=ins+1

###initilization
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
###Fuction definitions
def funcclick(x,y):
    lcor=int((x+300)/60)
    x=(lcor*60)-270
    wcor=int((y+300)/60)
    y=(wcor*60)-270
    cursor.goto(x,y)
    id=cursor.stamp()
    stampids.append(id)

def delete():
    lateststamp=len(stampids)
    cursor.clearstamp(stampids[lateststamp-1])






wn=turtle.Screen()
wn.onclick(funcclick)
wn.onkeypress(delete(),"z")
wn.mainloop()
wn.listen()