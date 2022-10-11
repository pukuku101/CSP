#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic","arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold"]
# adds the shapes to the turtles
for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.pensize(5)
  my_turtles.append(t)
  new_color = turtle_colors.pop()
  t.pencolor(new_color)
  t.fillcolor(new_color)
  

#  set position of first  turtle
startx = 25
starty = 100
angle = 0
#Moves turtle
for t in my_turtles:
  t.pu()
  t.goto(startx, starty)
  t.setheading(angle)
  t.pd()
  t.right(30)     
  t.forward(50)


#	changes start position
  startx = t.xcor()
  starty = t.ycor()
  angle = t.heading()

wn = trtl.Screen()
wn.mainloop()