import math 

def laskinsum(a, b):
    return a + b

def laskinerotus(a, b):
    return a - b

def laskinkerto(a, b):
    return a * b

def laskinjako(a, b):
    if b == 0:
        return "Vika: Nollalla jakaminen ei ole sallittua!"
    return a / b

def laskinpotenssi(a, b):
    return a ** b

def laskinmodulo(a, b):
    if b == 0:
        return "Vika: Nollalla jakaminen ei ole sallittua!"
    return a % b

def laskinkokonaisjako(a, b):
    if b == 0:
        return "Vika: Nollalla jakaminen ei ole sallittua!"
    return a // b

def laskinneliojuuri(a):
    if a < 0:
        return "Vika: Negatiivisen luvun neliöjuuri ei ole sallittu!"
    return math.sqrt(a)

def laskinkuutionjuuri(a):
    return a ** (1/3)

def laskinabsoluuttinen(a):
    return abs(a)

def laskinfaktoriaali(a):
    if a < 0 or int(a) != a:
        return "Vika: Faktoriaali vain ei-negatiivisille kokonaisluvuille!"
    return math.factorial(int(a))

def laskinlogaritmi(a):
    if a <= 0:
        return "Vika: Logaritmi vain positiivisille luvuille!"
    return math.log10(a)

def laskinln(a):
    if a <= 0:
        return "Vika: Ln vain positiivisille luvuille!"
    return math.log(a)

def laskinsuurin(a, b):
    return max(a, b)

def laskinpienin(a, b):
    return min(a, b)