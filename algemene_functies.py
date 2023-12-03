def mijn_functie_1(lange_lijst):
    a, b, c, d = lange_lijst
    return a*a, b*b, c*c, d*d 

print(mijn_functie_1([2, 4, 8, 12]))


def mijn_functie_2(korte_lijst):
    a, b = korte_lijst
    return a+b, a-b, a*b, a/b

print(mijn_functie_2([12,3]))
print(mijn_functie_2([12,2]))
print(mijn_functie_2([10,5]))
print(mijn_functie_2([100,20]))