#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#little things
font_setup=("Arial",20,"normal")
spot_color = "pink"
spot_size = 2
spot_shape = "circle"
scoretxt="Score:"
#functions
def spot_clicked(x,y):
    global timer_up
    if (timer_up==False):
        change_position()
    elif(timer_up==True):
        spot.hideturtle()
def change_position():
    newx=rand.randint(-350,350)
    newy=rand.randint(-300,300)
    spot.hideturtle()
    spot.goto(newx,newy)
    spot.showturtle()
    score_change()
#score function
def score_change():
    global score
    score+=1

    score_writer.clear()

    score_writer.write("Score:" + str(score), font=font_setup)
#timer function
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
#-----initialize turtle-----
spot = trtl.Turtle()
score_writer= trtl.Turtle()
counter =  trtl.Turtle()

score_writer.pu()
score_writer.hideturtle()
counter.hideturtle()
counter.pu()
counter.goto(230,300)
score_writer.goto(-350,300)
spot.shape(spot_shape)
spot.color(spot_color)
spot.shapesize(spot_size)
#-----game functions--------
score=0

#-----events----------------
spot.pu()
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()