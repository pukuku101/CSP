import random as rand
import turtle as trtl
###------variable definitions-----###
clickps=1000
global clicks
clicks=0
cpc=1
away_clicks=0
cur="200.gif"
font_setup=("Arial",20,"normal")
item_list=[]
item_price=[5,10]
turtles_list=[]
price=item_price.pop(0)
turnum=0
###------Function Definitions-----###
def automatic_income():
    global clicks
    clicks=clicks + away_clicks
    print(clicks)
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
        price2=round(price*1.8)
        item_price.insert(turnum,price2)
        clicks= clicks-price
        cpc=cpc+1
        score_change()
        price=item_price.pop(turnum)
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
score_counter
turtles_list.append(item)
turtles_list.append()


###-------Shop--------###
item.pu()
item.goto(300,200)
print_description(item)
###-------Events------------_###
cursor.onclick(cursor_clicked)
item.onclick(item_clicked)
wn.ontimer(automatic_income, clickps)
wn.mainloop()
