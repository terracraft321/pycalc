import pytest
from laskin import *

def testi_summa():
    assert laskinsum(2, 3) == 5
    assert laskinsum(-1, -4) == -5

def testi_vahennys():
    assert laskinerotus(5, 3) == 2
    assert laskinerotus(3, 5) == -2

def testi_kertolasku():
    assert laskinkerto(4, 3) == 12
    assert laskinkerto(-2, 5) == -10

def testi_jako():
    assert laskinjako(10, 2) == 5
    assert laskinjako(7, 2) == 3.5
    assert laskinjako(5, 0) == "Error: Nollalla jakaminen ei ole sallittua!"
    
def testi_potenssi_ja_modulo():
    assert laskinpotenssi(2, 3) == 8
    assert laskinpotenssi(5, 0) == 1
    assert laskinpotenssi(2, -2) == 0.25
    assert laskinmodulo(10, 3) == 1
    assert laskinmodulo(5, 0) == "Error: Nollalla jakaminen ei ole sallittua!"

def testi_kokonaisjako():
    assert laskinkokonaisjako(10, 3) == 3
    assert laskinkokonaisjako(5, 0) == "Error: Nollalla jakaminen ei ole sallittua!"

def testi_neliojuuri():
    assert laskinneliojuuri(9) == 3
    assert laskinneliojuuri(0) == 0
    assert laskinneliojuuri(-4) == "Error: Negatiivisen luvun neliöjuuri ei ole sallittu!"

def testi_kuutionjuuri():
    assert round(laskinkuutionjuuri(27), 5) == 3
    assert round(laskinkuutionjuuri(-27), 5) == -3

def testi_absoluuttinen():
    assert laskinabsoluuttinen(5) == 5
    assert laskinabsoluuttinen(-7) == 7

def testi_faktoriaali():
    assert laskinfaktoriaali(5) == 120
    assert laskinfaktoriaali(0) == 1
    assert laskinfaktoriaali(-3) == "Error: Faktoriaali vain ei-negatiivisille kokonaisluvuille!"
    assert laskinfaktoriaali(3.5) == "Error: Faktoriaali vain ei-negatiivisille kokonaisluvuille!"

def testi_logaritmi():
    assert laskinlogaritmi(100) == 2
    assert laskinlogaritmi(0) == "Error: Logaritmi vain positiivisille luvuille!"
    assert laskinlogaritmi(-5) == "Error: Logaritmi vain positiivisille luvuille!"

def testi_ln():
    import math
    assert laskinln(math.e) == 1
    assert laskinln(-1) == "Error: Ln vain positiivisille luvuille!"
    assert laskinln(0) == "Error: Ln vain positiivisille luvuille!"

def testi_suurin_ja_pienin():
    assert laskinsuurin(5, 10) == 10
    assert laskinpienin(5, 10) == 5
    assert laskinsuurin(-3, -7) == -3
    assert laskinpienin(-3, -7) == -7