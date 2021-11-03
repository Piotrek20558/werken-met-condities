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

if int(Vraag1) >=4 or int(Vraag2) >=5 or int(Vraag3) >=3 or Vraag4 == "y" or Vraag5 == "y" or Vraag6 == "y" or Vraag7 == "y" or Vraag8 >10 or Vraag10 >20 or Vraag11 >90 or Vraag12 == "y":
 print('U komt in aanmerking voor een sollicitatiegesprek, stuur snel uw CV.')

else:
    print('U voldoet niet aan onze strenge eisen voor deze functie, het spijt ons.')