import pytest
from laskin import (
    laskinsum,
    laskinerotus,
    laskinkerto,
    laskinjako,
    laskinpotenssi,
    laskinmodulo,
    laskinkokonaisjako,
    laskinneliojuuri,
    laskinkuutionjuuri,
    laskinabsoluuttinen,
    laskinfaktoriaali,
    laskinlogaritmi,
    laskinln,
    laskinsuurin,
    laskinpienin
)
def test_laskinsum_positive():
    assert laskinsum(2, 3) == 5 
def test_laskinsum_negative():
    assert laskinsum(-1, -4) == -5
def test_laskinsum_mixed():
    assert laskinsum(-2, 5) == 3

def test_laskinerotus_positive():
    assert laskinerotus(5, 3) == 2
    
def test_laskinerotus_negative():
    assert laskinerotus(3, 5) == -2

def test_laskinkerto_positive():
    assert laskinkerto(4, 3) == 12

def test_laskinkerto_negative():
    assert laskinkerto(-2, 5) == -10

def test_laskinkerto_zero():
    assert laskinkerto(0, 5) == 0

def test_laskinjako_positive():
    assert laskinjako(10, 2) == 5

def test_laskinjako_float():
    assert laskinjako(7, 2) == 3.5

def test_laskinjako_zero_division():
    assert laskinjako(5, 0) == "Error: Nollalla jakaminen ei ole sallittua!"

def test_laskinpotenssi_positive():
    assert laskinpotenssi(2, 3) == 8

def test_laskinpotenssi_zero_exponent():
    assert laskinpotenssi(5, 0) == 1

def test_laskinpotenssi_zero_base():
    assert laskinpotenssi(0, 5) == 0

def test_laskinpotenssi_negative_exponent():
    assert laskinpotenssi(2, -2) == 0.25
    
def test_laskinmodulo_positive():
    assert laskinmodulo(10, 3) == 1

def test_laskinmodulo_zero_division():
    assert laskinmodulo(5, 0) == "Error: Nollalla jakaminen ei ole sallittua!"

def test_laskinkokonaisjako_positive():
    assert laskinkokonaisjako(10, 3) == 3

def test_laskinkokonaisjako_zero_division():
    assert laskinkokonaisjako(5, 0) == "Error: Nollalla jakaminen ei ole sallittua!"
    
def test_laskinneliojuuri_positive():
    assert laskinneliojuuri(9) == 3

def test_laskinneliojuuri_zero():
    assert laskinneliojuuri(0) == 0

def test_laskinneliojuuri_negative():
    assert laskinneliojuuri(-4) == "Error: Negatiivisen luvun neliöjuuri ei ole sallittu!"

def test_laskinkuutionjuuri_positive():
    assert round(laskinkuutionjuuri(27), 5) == 3

def laskinkuutionjuuri(a):
    if a >= 0:
        return a ** (1/3)
    else:
        return -((-a) ** (1/3))

def test_laskinabsoluuttinen_positive():
    assert laskinabsoluuttinen(5) == 5

def test_laskinabsoluuttinen_negative():
    assert laskinabsoluuttinen(-7) == 7

def test_laskinfaktoriaali_positive():
    assert laskinfaktoriaali(5) == 120

def test_laskinfaktoriaali_zero():
    assert laskinfaktoriaali(0) == 1

def test_laskinfaktoriaali_negative():
    assert laskinfaktoriaali(-3) == "Error: Faktoriaali vain ei-negatiivisille kokonaisluvuille!"

def test_laskinfaktoriaali_float():
    assert laskinfaktoriaali(3.5) == "Error: Faktoriaali vain ei-negatiivisille kokonaisluvuille!"

def test_laskinlogaritmi_positive():
    assert laskinlogaritmi(100) == 2

def test_laskinlogaritmi_invalid():
    assert laskinlogaritmi(0) == "Error: Logaritmi vain positiivisille luvuille!"

def test_laskinln_positive():
    import math
    assert laskinln(math.e) == 1

def test_laskinln_invalid():
    assert laskinln(-1) == "Error: Ln vain positiivisille luvuille!"

def test_laskinsuurin():
    assert laskinsuurin(5, 10) == 10

def test_laskinpienin():
    assert laskinpienin(5, 10) == 5