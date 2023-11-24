from helper import decoreer

def print_aanbieding():
    prijzen = {
        "aardbei" :3,
        "vanille": 4,
        "chocolade": 5
    }

    aanbieding = prijzen["aardbei"] * 0.8

    reclame_text = f"Vandaag in de aanbieding: vaille-ijs, 1 liter - slechts € {aanbieding}"

    reclame_text2 = reclame_text[:63]

    reclame_text3 = reclame_text2.upper()

    reclame_text4 = reclame_text3.split()

    for el in reclame_text4:
        if len(el) >4:
            print(el.upper())
        else:
            print(el.lower())
            
decoreer("Aanbieding")
print_aanbieding()

            
