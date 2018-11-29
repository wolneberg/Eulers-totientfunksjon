"""
Dette program lager en .csv fil utifra .txt filen i https://raw.githubusercontent.com/wolneberg/Eulers-totientfunksjon/master/Skriving%20av%20csv%20fil/textfil.txt
som igjen har de samme verdiene som tabellen i http://primefan.tripod.com/Phi500.html
"""

import urllib.request    # For å bruke urllib.request.urlopen()

tekst = urllib.request.urlopen("https://raw.githubusercontent.com/wolneberg/Eulers-totientfunksjon/master/Skriving%20av%20csv%20fil/textfil.txt")

import pylab as pl    # For å bruke pl.loadtxt()

data = pl.loadtxt(tekst,  str)    # "data" blir en array med 3 kolonner der elementene er strenger

første = []    # Første kolonne
andre = []    # Andre kolonne
tredje=[]    # Tredje kolonne

for x in data[:,0]:          # Første kolonne blir heltallene n
    første.append(int(x))

for x in data[:,1]:         # Andre kolonne blir heltallene phy(n)
    andre.append(int(x))

for x in data[:,2]:     # Tredje kolonne blir en liste av heltallene som er faktorer av n
    x = x.split(",")
    x = [int(i) for i in x]
    tredje.append(x)

tabellen = []    # den endelige tabellen, som egentlig blir en liste av lister

for x in range(0,500):           # Hver rad i "tabellen" blir fylt inn
    rad = [første[x], andre[x], tredje[x]]
    tabellen.append(rad)

import pandas as pd

columns = ["n","phy(n)","faktorer"]    # Kolonnene i tabellen 

dataframe = pd.DataFrame(tabellen, columns = columns)    # "tabellen" gjøres om til en pandas dataframe

dataframe.to_csv("Euler500verdier.csv")
