age=int(input("age?"))
month=int(input("month"))
currentmonth=int(input("Currentmonth?"))
#determining how many days there are
if (month==1):
    extra_days=365
if (month==2):
    extra_days=337
if (month==3):
    extra_days=306
if (month==4):
    extra_days=276
if (month==5):
    extra_days=245
if (month==6):
    extra_days=214
if (month==7):
    extra_days=184
if (month==8):
    extra_days=153
if (month==9):
    extra_days=122
if (month==10):
    extra_days=92
if (month==11):
    extra_days=61
if (month==12):
    extra_days=31
if (month==1):
    nodays=365
if (month)==2):
    nodays=337
if (month==3):
    nodays=306
if (month==4):
    nodays=276
if (month==5):
    nodays=245
if (month==6):
    nodays=214
if (month==7):
    nodays=184
if (month==8):
    nodays=153
if (month==9):
    nodays=122
if (month==10):
    nodays=92
if (month==11):
    nodays=61
if (month==12):
    nodays=31

extra_days=(extra_days-nodays)
days = age*365
decades=age/10
weeks=age*52
minutes=days*60*60
print(days," days")
print(decades, " decades")
print(weeks," weeks")
print(minutes," minutes")
