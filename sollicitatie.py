Vraag0 = input('Wat is uw naam?')
Vraag1 = int(input('Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?'))
Vraag2 = int(input('Hoeveel jaar ervaring heeft u met jongleren?'))
Vraag3 = int(input('Hoeveel praktijkervaring heeft u met acrobatiek?'))
Vraag4 = input('Bent u in bezit van een Diploma MBO-4 ondernemen?')
Vraag5 = input('Bent u in bezit van een geldig Vrachtwagen rijbewijs?')
Vraag6 = input('Bent u in bezit van een hoge hoed?')
Vraag7 = input('Bent u een man of vrouw?')
if  Vraag7 == "m":
    Vraag8 = int(input('Hoelang is uw snor?'))
else:
    Vraag10 = int(input('Hoelang is uw haar?'))
Vraag11 = int(input('Hoe zwaar bent u?'))
Vraag12 = int(input('Hoelang bent u?'))
Vraag13 = input('Heeft u Certificaat “Overleven met gevaarlijk personeel?')
Vraag14 = input('Hoe oud bent u?')
Vraag15 = input('Hoeveel jaar verwacht u hier te gaan werken?')

if ((Vraag1 >=4 or Vraag2 >=5 or Vraag3 >=3) and Vraag4 == "y" and Vraag5 == "y" and Vraag6 == "y" and Vraag8 >10 and Vraag10 >20 and Vraag11 >90 and Vraag12 >150 and Vraag13 == "y" and Vraag14 <=18 and Vraag15 >=1):
 print('U komt in aanmerking voor een sollicitatiegesprek, stuur snel uw CV.')

else:
    print('U voldoet niet aan onze strenge eisen voor deze functie, het spijt ons.')