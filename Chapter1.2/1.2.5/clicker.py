import random as rand
import turtle as trtl
###------variable definitions-----###
clickps=1000
global clicks
clicks=0
cpc=1
away_clicks=0
cur="200.gif"
price=5
###------Function Definitions-----###

def automatic_income():
    global clicks
    clicks=clicks + away_clicks
    print(clicks)
def cursor_clicked(x,y):
    global clicks
    clicks=clicks + cpc
    print(clicks)
def item_clicked():
    if (clicks>=price):
        clicks= clicks-price
        cpc=cpc+1
        price=price*1.2

###------Initializer--------------###
wn=trtl.Screen()
wn.addshape(cur)
wn.bgpic("giphy.gif")
cursor=trtl.Turtle(shape=cur)
item=trtl.Turtle()

item.pu()
item.goto(200,200)
###-------Events------------_####
cursor.onclick(cursor_clicked)
wn.ontimer(automatic_income, clickps)
wn.mainloop()
