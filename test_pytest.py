import test_pytest

from laskin import (
    laskinsum,
    laskinerotus,
    laskinkerto,
    laskinjako,
    laskinpotenssi
)

def test_sum_normaali_syoete():
    """Testitapaus 1: Ekvivalenssiositus, normaali syöte"""
    assert laskinsum(5, 3) == 8


def test_jako_nollalla():
    """Testitapaus 2: Raja-arvoanalyysi, nollalla jakaminen"""
    assert laskinjako(10, 0) == "Error: Nollalla jakaminen ei ole sallittua!"


def test_kertolasku_negatiiviset():
    """Testitapaus 3: Ekvivalenssiositus, negatiiviset luvut"""
    assert laskinkerto(-4, -2) == 8


def test_potenssi_b_nolla():
    """Testitapaus 4: Raja-arvoanalyysi, b = 0"""
    assert laskinpotenssi(7, 0) == 1


def test_jako_normaali_polku():
    """Testitapaus 5: White Box, jakolaskun normaali polku"""
    assert laskinjako(9, 3) == 3
