def Omskriving(dataframe):    # skriver divisorstrenger om til divisorlister
    from pandas import Series
    divisorer = list(dataframe["divisorer"])
    for x in range(0,len(divisorer)):
        divisorer[x] = divisorer[x].split(",")
        for y in range(0,len(divisorer[x])):
            divisorer[x][y] = int(divisorer[x][y])
    
    del dataframe["divisorer"]
    kolonne = Series(divisorer)
    dataframe["divisorer"] = kolonne.values
    
    return dataframe
    
