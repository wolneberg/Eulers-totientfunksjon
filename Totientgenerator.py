# Denne funksjon genererer en pandas dataframe med tre kollonner og et gitt antall rader
# der den forste kollonnen er naturlige tall n fra og med 1 til og med et gitt 
# antall, den andre kollonnen er hvor mange tall mindre enn n som er innbyrdes 
# primske med tallet n, og den tredje kollonen er en liste av alle faktorer av
# n. Denne kan så gjores om til en .csv fil og analyseres

# Av Espen Sales
# 26/11/2018

import pandas as pd

maxverdi = 1000

nliste = [1]
phyliste = [1]
faktorliste = [[1]]

for x in range(2,maxverdi+1):
    n = x
    phy = 0
    faktorer = []
    for y in range(1,x+1):
        if x%y == 0:
            faktorer.append(y)
    
    for y in faktorliste:
        innbyrdes = True
        for z in range(1,len(faktorer)):
            if faktorer[z] in y:
                innbyrdes = False
        if innbyrdes == True:
            phy += 1
    
    nliste.append(n)
    phyliste.append(phy)
    faktorliste.append(faktorer)

tabell = []
for x in range(0,maxverdi):
    rad = [nliste[x],phyliste[x],faktorliste[x]]
    tabell.append(rad)

tabell.insert(0,[0,0,[0]])
    
#for x in tabell:
#    print(x)

kolonner = ["n","phy(n)","faktorer"]

dataframe = pd.DataFrame(tabell, columns = kolonner)
