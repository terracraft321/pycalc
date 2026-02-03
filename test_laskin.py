import pytest
from laskin import (
    laskinsum,
    laskinerotus,
    laskinkerto,
    laskinjako,
    laskinpotenssi
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