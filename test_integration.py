import math
from laskin import *

def testi_peruslasku():
    a = laskinsum(5, 3)          # 8
    b = laskinkerto(a, 2)        # 16
    c = laskinjako(b, 4)         # 4
    tulos = laskinneliojuuri(c)  # 2
    assert tulos == 2

def testi_negatiivisen_kuutionjuuri():
    tulos = laskinkuutionjuuri(-27)  # Oikea vastaus -3
    assert round(tulos, 5) == -3

def testi_voitto_ja_vero():
    tulot = 1200
    kulut = 300
    voitto = laskinerotus(tulot, kulut)  # 900
    vero = laskinkerto(voitto, 0.2)     # 180
    nettotulo = laskinerotus(voitto, vero)  # 720
    assert nettotulo == 720

def testi_monimutkainen_lasku():
    arvo = laskinsum(2, 3)              # 5
    arvo = laskinpotenssi(arvo, 3)      # 125
    arvo = laskinmodulo(arvo, 7)        # 6
    arvo = laskinkokonaisjako(arvo, 2)  # 3
    arvo = laskinabsoluuttinen(arvo - 5) # 2
    assert arvo == 2

def testi_nollalla_jakaminen():
    tulos = laskinjako(laskinkerto(10, 5), 0)
    assert tulos == "Error: Nollalla jakaminen ei ole sallittua!"

def testi_faktoriaali_ja_logaritmi():
    fakt = laskinfaktoriaali(5)          # 120
    log_val = laskinlogaritmi(fakt)      # log10(120)
    assert round(log_val, 5) == round(math.log10(120), 5)

def testi_ln_ja_potenssi():
    ln_val = laskinln(math.e ** 3)        # ln(e^3) = 3
    exp_val = laskinpotenssi(2, ln_val)   # 2^3 = 8
    assert round(exp_val, 5) == 8

def testi_virhe_faktoriaali_negatiivisella():
    tulos = laskinfaktoriaali(-2)
    assert tulos == "Error: Faktoriaali vain ei-negatiivisille kokonaisluvuille!"

def testi_suurin_ja_pienin():
    suurin = laskinsuurin(10, 7)  # 10
    pienin = laskinpienin(3, 8)   # 3
    tulos = laskinerotus(suurin, pienin)  # 7
    assert tulos == 7

def testi_summa_negatiivisella():
    assert laskinsum(-5, 3) == -2

def testi_kertolasku_negatiivisilla():
    assert laskinkerto(-4, 2) == -8
    assert laskinkerto(-4, -2) == 8

def testi_vahennys_negatiiviseksi():
    assert laskinerotus(3, 5) == -2

def testi_suurin_ja_pienin_negatiivisilla():
    assert laskinsuurin(-3, -7) == -3
    assert laskinpienin(-3, -7) == -7

def testi_logaritmi_ln_negatiivisilla():
    assert laskinlogaritmi(-5) == "Error: Logaritmi vain positiivisille luvuille!"
    assert laskinln(-1) == "Error: Ln vain positiivisille luvuille!"

def testi_neliojuuri_negatiivisella():
    assert laskinneliojuuri(-9) == "Error: Negatiivisen luvun neliöjuuri ei ole sallittu!"