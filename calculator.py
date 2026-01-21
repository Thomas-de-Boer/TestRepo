import berekeningen

verder = True


while verder == True:
    getal_error = False
    bewerking = input("Welke bewerking wil je uitvoeren? (optellen, aftrekken, vermenigvuldigen, delen): ")
    try:
        getal_1 = int(input("Voer het eerste getal in: "))
        getal_2 = int(input("Voer het tweede getal in: "))
    except:
        getal_error = True

    if getal_error == True:
        print("Er is een ongeldig nummer ingevoerd")

    elif bewerking == "optellen":
        resultaat = berekeningen.optellen(getal_1, getal_2)
        print(f"het resultaat is: {resultaat}")

    elif bewerking == "aftrekken":
        resultaat = berekeningen.aftrekken(getal_1, getal_2)
        print(f"het resultaat is: {resultaat}")

    elif bewerking == "vermenigvuldigen":
        resultaat = berekeningen.vermenigvuldigen(getal_1, getal_2)
        print(f"het resultaat is: {resultaat}")

    elif bewerking == "delen":
        resultaat = berekeningen.delen(getal_1, getal_2)
        if resultaat != False:
            print(f"het resultaat is: {resultaat}")

    else:
        print(f"{bewerking} is geen geldige bewerking.")


    while verder != False:
        verder_vraag = input("wil je nog een berekening doen? (ja/nee): ")
        if verder_vraag == "ja":
            verder = True
            break
        elif verder_vraag == "nee":
            verder = False
        else:
            print("vul een geldig antwoord in.")