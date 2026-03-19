def caesar(c,tekst):
    shift = c % 26
    tekstwyj = str()
    for i in range(len(tekst)):
        if tekst[i].isalpha() == True:
            if ord(tekst[i])>=65 and ord(tekst[i])<=90:
                znak = ord(tekst[i])+shift
                while znak > 90:
                    znak = znak -26
                while znak < 65:
                    znak = znak +26
            tekstwyj = tekstwyj + chr(znak)
            
        else:
            tekstwyj = tekstwyj + tekst[i]
    return tekstwyj

wiad = caesar(10,"ABD12!")

print(wiad)
