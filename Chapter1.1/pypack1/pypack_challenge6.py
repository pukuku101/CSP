initial = int(input("Number of initial Zombies"))
pz = int(input("How many days since Patient Zero?"))
rate=int(input("How many does each zombie infect in a day?"))
for i in range(pz):
    initial = initial*(rate+1)
print(initial)
