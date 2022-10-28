import random
import webbrowser
pool=int(input("How much are you coming to the table with? (not betting on this hand)"))
keep_playing = "y"
while (keep_playing=="y"):
    win_state=2
    bet=int(input("How much are you betting?"))
    p3=0
    p4=0
    d3=0
    d1 = random.randint(2,11)
    d2 = random.randint(2,11)
    p1 = random.randint(2,11)
    p2 = random.randint(2,11)
    if p1==11:
        p1="A"
    if p2==11:
        p2="A"
    print("Dealer: ",d1,",#")
    print("You: ",p1,p2)
    x=int(input("hit(1)or stay(2)"))
    if (x==1):
        p3=random.randint(2,11)
        if(p3==11):
            p3="A"
        print("You: ",p1,p2,p3)
        if (p1 == "A"):
            p1=1
        if (p2=="A"):
            p2 = 1
        if (p3=="A"):
            p3 = 1
        x=input("hit(1)or stay(2)")
        if (x==1):
            p4=random.randint(2,11)
            if(p4==11):
                p4="A"
            if (p1 == 1):
                p1="A"
            if (p2==1):
                p2 = "A"
            if (p3==1):
                p3 = "A"
            print("You: ",p1,p2,p3,p4)
            if(p4=="A"):                    
                p4=1
    if (p1 == "A"):
        p1=1
    if (p2=="A"):
        p2 = 1
    if (p3=="A"):
        p3 = 1
    if (p1+p2+p3+p4<=21):
        if (d1+d2<=16):
            d3 = random.randint(2,11)
            if (d3==11):
                d3="A"
        print("Dealer: ",d1,",#",d3)
    if(d1=="A"):
        d1=1
    if(d2=="A"):
        d2=1
    if(d3=="A"):
        d3=1
    if(d1+d2+d3>=22):
        print("Dealer Busted!")
        win_state=0
    if (d1==1):
        if(d1+d2+d3<=11):
            d1=11
    if (d2==1):
        if(d1+d2+d3<=11):
            d2=11
    if (d3==1):
        if(d1+d2+d3<=11):
            d3=11
    if (p1 == 1):
        p1="A"
    if (p2==1):
        p2 = "A"
    if (p3==1):
        p3 = "A"
    if (p4==1):
        p4 = "A"
    if (p1=="A"):
        p1 = int(input("What is your ace? 1 or 11?"))
    if (p2=="A"):
        p2 = int(input("What is your ace? 1 or 11?"))
    if (p3=="A"):
        p3 = int(input("What is your ace? 1 or 11?"))
    if (p4=="A"):
        p4 = int(input("What is your ace? 1 or 11?"))
    if(p1+p2+p3+p4>=22):
        win_state=1
        print("You Busted!")
    if (win_state==0):
        d1=0
        d2=0
        d3=0
    if (win_state==1):
        p1=0
        p2=0
        p3=0
        p4=0
    elif(p1+p2+p3+p4>=d1+d2+d3):
        win_state=0
    elif(p1+p2+p3+p4<=d1+d2+d3+1):
        win_state=1
    if (d1==1):
        d1="A"
    if (d1==11):
        d1="A"
    if (d2==1):
        d2="A"
    if (d2==11):
        d2="A"
    if (d3==1):
        d3="A"
    if (d3==11):
        d3="A"
    print("Dealer: ",d1,d2,d3)

    print("You: ",p1,p2,p3,p4)

    if(win_state==0):
        print("You won! you earned $",bet/2,"!")
        pool = pool + (bet/2)
    elif(win_state==1):
        print("You lost! You lost $",bet,"!")
        pool= pool - bet
    keep_playing=input("Keep playing? (y/n)")
    print("Money left: $",pool)
print("Thanks for playing!!!")
webbrowser.open("www.gamingaddictsanonymous.org")