import turtle as trtl


# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)
# legs
legs = 6
leg_length = 50
angle = 160
ladybug.pensize(5)
rep = 0
pair = 0
while (rep < .5*legs):
    ladybug.goto(0,-30)
    ladybug.setheading(angle)
    ladybug.forward(leg_length)
    angle = angle + 30
    rep = rep + 1
rep = 0
angle = angle + 60
while (rep < .5*legs):
    ladybug.goto(0,-30)
    ladybug.setheading(angle)
    ladybug.forward(leg_length)
    angle = angle +30
    rep = rep + 1
ladybug.setheading(0)
# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  ypos = ypos + 25
  xpos = xpos + 5
  num_dots = num_dots + 1

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()
