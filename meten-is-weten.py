a = int(input('voer een geheel getal A'))
b = int(input('voer een geheel getal B'))



if a > b:
    max = a
    min = b
    print('Het minimum is:' + str(min))
    print('Het maximum is:' + str(max))
elif b > a:
    max = b
    min = a
    print('Het minimum is:' + str(min))
    print('Het maximum is:' + str(max))
else:
    print('a en b zijn even groot')
