#   a123_apple_1.py
import turtle as trtl
import random as rand
#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
x=0
y=0
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file

def draw_apple(active_apple):
  active_apple.shape(apple_image)
  apple.showturtle()
  apple_letter()
  wn.update()



alphabet=["a","b","c"]

def apple_fall():
  y2=apple.ycor()
  apple.setheading(0)
  apple.pu()
  apple.rt(90)
  apple.fd(y2+140)
  apple.clear()
  apple.hideturtle()
  x=rand.randint(-200,200)
  y=rand.randint(-20,200)
  apple.goto(x,y)
  apple.showturtle()
  
letters=rand.choice(alphabet)


def apple_letter():
  apple.write(letters, font=("Arial",74,"bold"))
#-----function calls-----
wn.bgpic("background.gif")

draw_apple(apple)
wn.onkeypress(apple_fall, letters)
wn.listen()
wn.mainloop()