import random as rand
import turtle as trtl
###------variable definitions-----###
clickps=1000
global clicks
clicks=0
cpc=1
away_clicks=0
font_setup=("Arial",20,"normal")
textprompt=50
dino="dino.gif"
cur="200.gif"
messages = ["                Having fun?","You realy like clicking, don't you?","Shouldnt you do something else?"]
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
    global textprompt
    if (clicks>=price):
        if (clicks>=textprompt):
            text_writer.clear()
            mesnum=rand.randrange(0,3)
            playertxt=messages.pop(mesnum)
            messages.insert(mesnum,playertxt)
            text_writer.write(playertxt,font=font_setup)
            textprompt=textprompt*2
        price2=round(price**1.3)
        clicks= clicks-price
        cpc=cpc+1
        score_change()
        price=price2

    print_description(item)


def score_change():
    score_counter.clear()
    score_counter.write("Clicks: " + str(clicks),font=font_setup)
def print_description(active_turtle):
    active_turtle.clear()
    active_turtle.write("Cost: "+str(price),font=font_setup)

###------Initializer--------###
wn=trtl.Screen()
wn.addshape(cur)
wn.addshape(dino)
wn.bgpic("giphy.gif")
wn.screensize(700,700)
###-------Turtles--------###
cursor=trtl.Turtle(shape=cur)
item=trtl.Turtle(dino)
score_counter=trtl.Turtle()
score_counter.hideturtle()
score_counter.pu()
score_counter.goto(-300,300)
text_writer=trtl.Turtle()
text_writer.pu()
text_writer.hideturtle()
text_writer.goto(-200,250)
###-------Shop--------###
item.pu()
item.goto(260,250)
print_description(item)
###-------Events------------_###
cursor.onclick(cursor_clicked)
item.onclick(item_clicked)
wn.mainloop()
