from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    verkoop_prijs = prijs * (1-korting)
    print(f"emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} voor {verkoop_prijs} euro.")
    return

def inkomsten_totaal(inkomsten, BTW):
    inkomsten = a + b + c + d + e + f + g
    BTW_2 = inkomsten * BTW
    print(f"het totaal van alle inkomsten van deze week is {inkomsten} euro, waarover {BTW_2} euro btw betaald dient te worden.")
    return

def laag_en_hoog(mijn_lijst):
    fun_min = min(mijn_lijst)
    fun_max = max(mijn_lijst)
    return fun_min, fun_max

def gemiddelde(mijn_lijst):
    bedrag = ((sum(mijn_lijst))/len(mijn_lijst))
    return bedrag
       
def meervoudig(invoer_lijst):
    result = laag_en_hoog(invoer_lijst)
    print(result)    
    return result
    
def combinatie(invoerlijst_2):
    korte_lijst = meervoudig(invoerlijst_2)
    uitkomst = mijn_functie_2(korte_lijst)
    return uitkomst
    


a = 220
b = 430
c = 125
d = 160
e = 205
f = 90
g = 345

fun_min, fun_max = laag_en_hoog([220, 430, 125, 160, 205, 90, 345])
print([fun_min, fun_max])

variabelenlijst = [10, 5, 3, 2, 1, 2, 9]
meervoudig(variabelenlijst)

bedrag = gemiddelde([220, 430, 125, 160, 205, 90, 345])
print(f"De gemiddelde inkomsten van deze week zijn {bedrag} euro")

aanbieding_1("aardbei", 4, 0.1)  

inkomsten_totaal(0, 0.09)

uitkomst = combinatie(variabelenlijst)
print(uitkomst)
