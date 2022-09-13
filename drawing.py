#painter settings
import turtle as trtl

painter = trtl.Turtle()
painter.color("yellow")
painter.fillcolor("yellow")
#the head
painter.begin_fill()
painter.circle(50)
painter.end_fill()


#end of program
wn = trtl.Screen()
wn.mainloop()
