color_set=input("What will be the color theme of your flower arrangement?")

if (color_set=="blue"):
  theme=["blue","blue","navy","skyblue","cyan","deepskyblue"]
elif(color_set=="orange"):
  theme=["orange","orange","white","white"]
elif(color_set=="red"):
  theme=["red","red","maroon","violet"]
elif(color_set=="turquoise"):
  theme=["turquoise","turquoise","cyan","skyblue","white"]
elif(color_set=="purple"):
  theme=["purple","purple","purple","violet","violet","magenta","magenta"]
elif(color_set=="green"):
  theme=["lightgreen","green","green","darkgreen"]
elif(color_set=="yellow"):
  theme=["yellow","gold","yellow","white","white"]
for i in (theme):
  print(i)
