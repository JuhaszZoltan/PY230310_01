class Egitest:
    hol_kering:str
    elnevezes:str
    tavolsag:int
    direkt_irany:bool
    atmero:int
    felfedezo_neve:str
    felfedezes_eve:int

    def __init__(self, hol:str, eln:str, tav:int, dir:bool, atm:int, fn:str, fe:int):
        self.hol_kering = hol
        self.elnevezes = eln
        self.tavolsag = tav
        self.direkt_irany = dir
        self.atmero = atm
        self.felfedezo_neve = fn
        self.felfedezes_eve = fe