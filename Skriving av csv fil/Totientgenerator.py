def TotientGenerator(maxverdi):     # "maxverdi" er hvor mange rader .csv filen inneholder, altså hvor mange naturlige tall fra 1 til "maxverdi" som inkluderes
    from pandas import DataFrame

    nliste = [1]      # De tre kolonnene starter som lister, og inneholder verdiene for n=1
    phyliste = [1]
    faktorliste = [[1]]

    for x in range(2,maxverdi+1):    # Fra n=2 til og med "maxverdi" blir kolonnene forlenget 
        n = x
        phy = 0
        faktorer = []
        for y in range(1,x+1):    # Faktorene til n beregnes og legges til i listen av faktorer
            if x%y == 0:
                faktorer.append(y)

        for y in faktorliste:    # Med brute force sjekker programmet hvor mange tall mindre enn n som er innbyrdes primske med n
            innbyrdes = True
            for z in range(1,len(faktorer)):
                if faktorer[z] in y:
                    innbyrdes = False
            if innbyrdes == True:
                phy += 1

        nliste.append(n)        # Verdiene legges til sine respektive kolonner
        phyliste.append(phy)
        faktorliste.append(faktorer)

    tabell = []                    # Den endelige tabellen ferdigstilles 
    for x in range(0,maxverdi):
        rad = [nliste[x],phyliste[x],faktorliste[x]]
        tabell.append(rad)
        
    kolonner = ["n","phy(n)","faktorer"]
    filnavn = "Totient"+str(maxverdi)+"verdier.csv"         # "filnavn" er skrevet slik at navnet på .csv filen reflekterer hvor mange verdier av n er inkludert
    dataframe = pd.DataFrame(tabell, columns = kolonner)
    
    dataframe.to_csv(filnavn)    # .csv filen lagres i samme mappe som denne jupyter filen, funksjonen behøver ikke returnere noe
