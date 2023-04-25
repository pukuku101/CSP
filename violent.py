import matplotlib.pyplot as plt
violentcrimesfile=open('violentcrimes.txt')
crimelist = violentcrimesfile.readlines()
alcholabusefile=open("foodprice.txt")
pricelist=alcholabusefile.readlines()
print(crimelist)
print(pricelist)
seafood=[]
for i in range(len(crimelist)):
    crimelist[i]=int(crimelist[i])
for i in range(len(pricelist)):
    pricelist[i]=int(pricelist[i])
for i in range(len(pricelist)):
    tempreverse=pricelist.pop()
    seafood.append(tempreverse)
print(crimelist)
fig, axs=plt.subplots(2)
fig.suptitle("Rates of Robbery V.S. Reported Net Worth of Imported Sea Food In 100,000's")
axs[0].plot(range(2000,2020),crimelist,'b.-')
axs[0].axis([2000,2020,200000,500000])
axs[1].plot(range(2000,2020),seafood,'r.--')
axs[1].axis([2000,2020,9000,250000])
plt.xlabel("Years")
if (plt.waitforbuttonpress()==True):
    plt.suptitle("This correlation is undeniably important.")
if (plt.waitforbuttonpress()==True):
    plt.suptitle("Did You Expect More?")
plt.show()
violentcrimesfile.close()
alcholabusefile.close()
