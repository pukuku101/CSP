import random as rand
import turtle as trtl
###------variable definitions-----###
clickps=1000
global clicks
clicks=0
cpc=1
away_clicks=0
font_setup=("Arial",20,"normal")
textprompt=100

cur="200.gif"
messages = []
price=5
turnum=0
###------Function Definitions-----###
def cursor_clicked(x,y):
    global clicks
    clicks=clicks + cpc
    score_change()

def item_clicked(x,y):
    global clicks
    global price
    global cpc
    global turnum
    if (clicks>=price):
        config_turtles(x,y)
        price2=round(price*9)
        clicks= clicks-price
        cpc=cpc+1
        score_change()
        price=price2
        if (clicks>=textprompt):
            mesnum=rand.randrange(0,5)
            playertxt=messages.pop(mesnum)
            messages.insert(playertxt, mesnum)
            text_writer.write(playertxt,font=font_setup)
            textprompt=textprompt*7
    print_description(item)


def score_change():
    score_counter.clear()
    score_counter.write("Clicks: " + str(clicks),font=font_setup)
def print_description(active_turtle):
    active_turtle.clear()
    active_turtle.write("Cost: "+str(price),font=font_setup)
def config_turtles(x,y):
  if (x>=100 and x<=150 and y>=100 and y<=150):
    turnum=0
###------Initializer--------###
wn=trtl.Screen()
wn.addshape(cur)
wn.bgpic("giphy.gif")
###-------Turtles--------###
cursor=trtl.Turtle(shape=cur)
item=trtl.Turtle()
score_counter=trtl.Turtle()
score_counter.hideturtle()
score_counter.pu()
score_counter.goto(-300,300)
text_writer=trtl.Turtle()




###-------Shop--------###
item.pu()
item.goto(300,200)
print_description(item)
###-------Events------------_###
cursor.onclick(cursor_clicked)
item.onclick(item_clicked)
wn.mainloop()
