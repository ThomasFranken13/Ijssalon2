a = 2
b = 4
c = 8
d = 12

def mijn_functie_1():
    global a
    x = a * a   
    print(x)
    
    global b
    y = b * b
    print(y)
    
    global c
    z = c * c
    print(z)
    
    global d
    q = d * d
    print(q)
    
# mijn_functie_1()

e = 12
f = 3
g = 2
h = 10
i = 5
j = 100
k = 20

def mijn_functie_2():
    ResultA = e + f
    ResultB = e - f
    ResultC = e * f
    ResultD = e / f
    ResultE = e + g
    ResultF = e - g
    ResultG = e * g
    ResultH = e / g
    ResultI = h + i
    ResultJ = h - i
    ResultK = h * i
    ResultL = h / i
    ResultM = j + k
    ResultN = j - k
    ResultO = j * k
    ResultP = j / k
    print(ResultA, ResultB, ResultC, ResultD, ResultE, ResultF, ResultG, ResultH, ResultI, ResultJ, ResultK, ResultL, ResultM, ResultN, ResultO, ResultP)
    
mijn_functie_2()