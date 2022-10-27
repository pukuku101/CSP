import turtle as trtl
import random
pen=trtl.Turtle()
pen.speed(0)
z=0
x=-500
a=0
y=-300
color_set=input("What will be the color theme of your flower arrangement?")
#Arrangment themes
if (color_set=="blue"):
  theme=["blue","blue","navy","skyblue","cyan","deepskyblue","blue","navy","skyblue","cyan","deepskyblue"]
elif(color_set=="orange"):
  theme=["orange","orange","white","white","orange","orange","white",]
elif(color_set=="red"):
  theme=["red","red","maroon","violet","red","maroon","violet"]
elif(color_set=="turquoise"):
  theme=["turquoise","turquoise","cyan","skyblue","white","turquoise","cyan","skyblue","white"]
elif(color_set=="purple"):
  theme=["purple","purple","purple","violet","violet","magenta","magenta"]
elif(color_set=="green"):
  theme=["lightgreen","green","green","darkgreen","yellow","lightgreen","green","darkgreen",]
elif(color_set=="yellow"):
  theme=["yellow","gold","yellow","white","white"]


while (z<=38):
    color = random.choice(theme)
    pen.pu()
    pen.goto(x,y)
    pen.pencolor(color)
    pen.color(color)
    pen.fillcolor(color)
    pen.begin_fill()
#flowers
    for i in range(15):
        a=a+30
        pen.setheading(a)
        pen.circle(30,180)
    a=0
    pen.end_fill()
    pen.pu()
#seeds
    pen.goto(x-160,y-20)
    pen.pd()
    pen.color("black")
    if (color=="black"):
        pen.color("white")
        pen.fillcolor("white")
    pen.begin_fill()
    pen.circle(50)
    pen.end_fill()
    pen.color(color)
    if (x>=700):
        y =y+200
        x=-650
    x=x+150
    z=z+1
wn = trtl.Screen()
wn.bgcolor("black")
wn.mainloop()
