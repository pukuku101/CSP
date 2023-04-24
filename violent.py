import matplotlib.pyplot as plt
violentcrimesfile=open('violentcrimes.txt')
crimelist = violentcrimesfile.readlines()
alcholabusefile=open("alcholabuse.txt")
abuselist=alcholabusefile.readlines()
print(crimelist)
print(abuselist)
"""
for i in range(len(crimelist)):
    crimelist[i]=int(crimelist[i])
for i in range(len(abuselist)):
    abuselist[i]=int(abuselist[i])
print(crimelist)
plt.plot(range(1999,2019),crimelist,'b.-')
plt.axis([1999,2020,0,2000000])
plt.plot(range(2002,2018),abuselist,'r.--)
plt.xlabel("Years")
plt.ylabel("Number in Millions")
plt.title("Violent Crimes Committed in the U.S. Every Year")
plt.show()
"""
