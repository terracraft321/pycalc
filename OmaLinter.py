import sys
MAKSIMI_RIVIN_PITUUS = 50
virheet = 0
varoitukset = 0
määritellyt_muuttujat = [] 
nähdyt_vakiot = set()
def on_snake_case(nimi):
    if not nimi:
        return False
    if not (nimi[0].islower() or nimi[0] == "_"):
        return False
    for merkki in nimi:
        if not (merkki.islower() or merkki.isdigit() or merkki == "_"):
            return False
    return True
def on_isolla_kirjaimella(nimi):
    if not nimi:
        return False
    if not (nimi[0].isupper() or nimi[0] == "_"):
        return False
    for merkki in nimi:
        if not (merkki.isupper() or merkki.isdigit() or merkki == "_"):
            return False
    return True
try:
    with open('koodi.txt', 'r', encoding='utf-8') as tiedosto:
        rivit = tiedosto.readlines()
    try:
        compile("".join(rivit), 'koodi.txt', 'exec')
    except SyntaxError as e:
        print(f"VIRHE rivillä {e.lineno}: syntaksivirhe ({e.msg})")
        virheet += 1
    for i, rivi in enumerate(rivit, start=1):
        rivi_ilman_uutta_riviä = rivi.rstrip('\n')
        if "TODO" in rivi:
            print(f"VIRHE rivillä {i}: TODO löydetty!")
            virheet += 1
        if len(rivi_ilman_uutta_riviä) > MAKSIMI_RIVIN_PITUUS:
            print(f"VAROITUS rivillä {i}: Rivi yli {MAKSIMI_RIVIN_PITUUS} merkkiä")
            varoitukset += 1
        if rivi_ilman_uutta_riviä != rivi_ilman_uutta_riviä.rstrip():
            print(f"VAROITUS rivillä {i}: Rivin lopussa välilyönti")
            varoitukset += 1
        johtavat = rivi[:len(rivi)-len(rivi.lstrip())]
        if " " in johtavat and "\t" in johtavat:
            print(f"VAROITUS rivillä {i}: Tab ja välilyönti sekaisin sisennyksessä")
            varoitukset += 1
        if "=" in rivi and not rivi_ilman_uutta_riviä.lstrip().startswith("#"):
            osat = rivi.split("=")
            if len(osat) < 2:
                print(f"VIRHE rivillä {i}: Puuttuva muuttuja ennen '='")
                virheet += 1
                continue
            nimi = osat[0].strip()
            if nimi.isidentifier():
                määritellyt_muuttujat.append((nimi, i))
                if len(nimi) == 1:
                    print(f"VAROITUS rivillä {i}: Yksikirjaiminen muuttuja '{nimi}'")
                    varoitukset += 1
                if not on_snake_case(nimi) and not on_isolla_kirjaimella(nimi):
                    print(f"VAROITUS rivillä {i}: Huono muuttujan nimi '{nimi}'")
                    varoitukset += 1
                if on_isolla_kirjaimella(nimi):
                    if nimi in nähdyt_vakiot:
                        print(f"VAROITUS rivillä {i}: Vakio '{nimi}' yritetty uudelleen määrittää")
                        varoitukset += 1
                    nähdyt_vakiot.add(nimi)
        if rivi_ilman_uutta_riviä.lstrip().startswith("def "):
            if "(" not in rivi_ilman_uutta_riviä or ")" not in rivi_ilman_uutta_riviä:
                print(f"VIRHE rivillä {i}: Funktiossa puuttuvat sulut")
                virheet += 1
                continue
            funktio_nimi = rivi_ilman_uutta_riviä[4:rivi_ilman_uutta_riviä.index("(")].strip()
            if not on_snake_case(funktio_nimi):
                print(f"VAROITUS rivillä {i}: Huono funktion nimi '{funktio_nimi}'")
        if "print " in rivi and "(" not in rivi:
            print(f"VAROITUS rivillä {i}: print funktiota pitäisi käyttää sulkujen kanssa")
            varoitukset += 1
    for nimi, rivi_no in määritellyt_muuttujat:
        löytyi_jälkeen = any(nimi in l for l in rivit[rivi_no:])
        if not löytyi_jälkeen:
            print(f"HUOMIO rivillä {rivi_no}: Muuttuja '{nimi}' ei käytössä")
            varoitukset += 1
except FileNotFoundError:
    print("Tiedostoa koodi.txt ei löytynyt.")
    sys.exit(1)