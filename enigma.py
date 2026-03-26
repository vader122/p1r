def enigma(tekst, przes):

    if przes > 255 or przes<0:
        przes = przes % 256
    znaki = [x for x in tekst]
    znaki_kod = [ord(x) for x in znaki]
    znaki_szyfr = [x ^ przes for x in znaki_kod]
    znaki_szyfr_str = [str(x) for x in znaki_szyfr]
    lacznik = " "
    wyj = lacznik.join(znaki_szyfr_str)

    return wyj

print(enigma("Non intratur in veritatem, nisi per caritatem.", 7))

