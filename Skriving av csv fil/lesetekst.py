
import pylab as pl

data = pl.loadtxt("textfil.txt",  str)

første = []    # The first collumn
andre = []    # The second collumn
tredje=[]    # The third collumn

for x in data[:,0]:
    første.append(int(x))

for x in data[:,1]:
    andre.append(int(x))

for x in data[:,2]:
    x = x.split(",")
    x = [int(i) for i in x]
    tredje.append(x)

tabellen = []

for x in range(0,500):
    tabellen.append(list([]))
    tabellen[x].append(første[x])
    tabellen[x].append(andre[x])
    tabellen[x].append(tredje[x])
    
for x in tabellen:
    print(x)
    