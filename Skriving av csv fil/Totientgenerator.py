def TotientGenerator(maxverdi):
    from pandas import DataFrame
    
    nliste = [1]
    phyliste = [1]
    divisorlister = [[1]]
    divisorstrenger = ["1"]
    tabell = []
    
    for x in range(2,maxverdi+1):
        n = x
        phy = 0
        divisorer = []
        divisorstreng = ""
        
        for y in range(1,n+1):
            if n%y == 0:
                divisorer.append(y)
        
        for y in divisorer:
            divisorstreng = divisorstreng+str(y)+","
        divisorstreng = divisorstreng[0:len(divisorstreng)-1]
        
        for y in divisorlister:    # y er divisorlistene
            innbyrdes = True
            for z in divisorer:    # z er aktuelle divisorer
                if z != 1 and z in y:    # hvis z ikke er 1 og finnes i andre divisorlister
                    innbyrdes = False
            if innbyrdes == True:
                phy += 1
        
        nliste.append(n)
        phyliste.append(phy)
        divisorlister.append(divisorer)
        divisorstrenger.append(divisorstreng)
        
    tabell = []
    
    for x in range(0,maxverdi):
        rad = [nliste[x],phyliste[x],divisorstrenger[x]]
        tabell.append(rad)
    
    kolonner = ["n","phy(n)","divisorer"]
    filnavn = "totient"+str(maxverdi)+"n.csv"
    dataframe = DataFrame(tabell,columns = kolonner)
    dataframe.to_csv(filnavn,index=False)
    
