def aanbieding_1(smaak, prijs, korting):
    verkoop_prijs = prijs * (1-korting)
    print(f"emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} voor {verkoop_prijs} euro.")

aanbieding_1("aardbei", 4, 0.1)  


a = 220
b = 430
c = 125
d = 160
e = 205
f = 90
g = 345

def inkomsten_totaal(inkomsten, BTW):
    inkomsten = a + b + c + d + e + f + g
    BTW_2 = inkomsten * BTW
    print(f"het totaal van alle inkomsten van deze week is {inkomsten} euro, waarover {BTW_2} euro btw betaald dient te worden.")
    
inkomsten_totaal(0, 0.09)


