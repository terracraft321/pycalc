import os

def laskinsum(a, b):
    """Palauttaa a + b"""
    return a + b

def laskinerotus(a, b):
    """Palauttaa a - b"""
    return a - b

def laskinkerto(a, b):
    """Palauttaa a * b"""
    return a * b

def laskinjako(a, b):
    """Palauttaa a / b, tarkistaa nollajaon"""
    if b == 0:
        return "Error: Nollalla jakaminen ei ole sallittua!"
    return a / b

def laskinpotenssi(a, b):
    """Palauttaa a ** b"""

    return a ** b
