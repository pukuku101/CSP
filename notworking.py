#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl
# create two empty lists of turtles, adding to them later
global horiz_turtles
horiz_turtles = []
global vert_turtles
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:
#Horizontal turtle
  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)
#Vertical turtle
  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  
  tloc += 50

# TODO: move turtles across and down screen, stopping for collisions
for i in horiz_turtles:
  print(i)

for step in range(50):
  xcor1 = vt.xcor()
  xcor2 = ht.xcor()
  ycor1 = vt.ycor()
  ycor2 = ht.ycor()
  if (abs(xcor1-xcor2)<=20):
    if (abs(ycor1-ycor2)<=20):
      horiz_turtles.remove(ht)
      vert_turtles.remove(vt)
  else:
    ht.fd(3)
    vt.fd(3)




wn = trtl.Screen()
wn.mainloop()
