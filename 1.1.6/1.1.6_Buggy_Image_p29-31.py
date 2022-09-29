import turtle as trtl
painter = trtl.Turtle()
# Spider abdomen
painter.pensize(40)
painter.circle(20)
# Configure legs
legs = 8
leg_length = 70
angle = 180
painter.pensize(5)
rep = 0
pair = 0
# Drawing legs
while (rep < .5*legs):
    painter.goto(0,20)
    painter.setheading(angle)
    painter.forward(leg_length)
    angle = angle + 30
    rep = rep + 1
rep = 0
angle = angle + 60
while (rep < .5*legs):
    painter.goto(0,20)
    painter.setheading(angle)
    painter.forward(leg_length)
    angle = angle +30
    rep = rep + 1
#eyes
painter.pencolor("red")
painter.pu()
painter.goto(5,-10)
painter.pd()
painter.circle(1)
painter.pu()
painter.goto(35,20)
painter.pd()
painter.circle(1)
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()
