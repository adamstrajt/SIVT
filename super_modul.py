def super_funkce() -> None:
    print("ja jsem super funkce")

#print("ja jsem super modul")
#super_funkce()

posledni_vysledek = 0
pamet = 0

def plus(a: float,b: float) -> float:
    global posledni_vysledek 
    posledni_vysledek = a+b
    return posledni_vysledek

def multi(a: float,b: float) -> float:
    global posledni_vysledek 
    posledni_vysledek = a*b
    return posledni_vysledek

def uloz_vysledek() -> None:
    #uklada vysledek posledni operace do pameti
    global posledni_vysledek
    global pamet
    pamet = posledni_vysledek
    return

def vrat_pamet() -> float:
    # vraci obsah pameti

    pass

def pricti_k_pameti(op: float) -> None:
    # pricte k pameti "op"
    pass

def vynasob_s_pameti(op: float) -> None:
    # vynasobi s pameti "op"
    pass
