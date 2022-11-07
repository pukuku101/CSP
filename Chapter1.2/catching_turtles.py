#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb

#-----game configuration----
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
leaderboard_file_name = "a122_leaderboard.txt"
player_name=input("Name?")
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
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
def manage_leaderboard():

  global score
  global spot

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

  else:lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)

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
