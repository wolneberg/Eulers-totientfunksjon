"""
Denne funksjonen lager en pandas dataframe med kolonner n, phy(n) og faktorer av n for alle naturlige tall fra 1 til "maxverdi"
"""

def TotientGenerator(maxverdi):
    from pandas import DataFrame

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
    kolonner = ["n","phy(n)","faktorer"]
    dataframe = pd.DataFrame(tabell, columns = kolonner)
    return dataframe
