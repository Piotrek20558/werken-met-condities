Vraag1 = input('Is de kaas geel?')

if Vraag1 == "yes":
    Vraag5 = input('Zitten er gaten in?')
    if Vraag5 == "yes":
        Vraag6 = input('Is de kaas belachelijk duur?')
        if Vraag6 == "yes":
            print('Emmenthaler')
        else:
            print('Leerdammer')

    else:
        Vraag7 = input('Is de kaas hard als een steen?')
        if Vraag7 == "yes":
            print('Pammigiano Reggiano')
        else:
            print('Goudse Kaas')

if Vraag1 == "no":
    Vraag2 = input('Heeft de kaas blauwe schimmels?')
    if Vraag2 =="no":
       Vraag3 = input('Heeft de kaas korst?')
       if Vraag3 =="yes":
            print('Camembert')
       else:
            print('Mozzarella')
    else:
        Vraag4 = input('Heeft de kaas een korst?')
        if Vraag4 == "yes":
            print("Bleu de Rochbaron")
        else:
            print("Foume d'Ambert")