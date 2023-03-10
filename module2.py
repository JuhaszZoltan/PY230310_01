class Egitest:
    def __init__(self, beolvasott_sor:str):
        darabok:list[str] = beolvasott_sor.strip().split(';')
        self.hol_kering:str = darabok[0]
        self.elnevezes:str = darabok[1]
        self.tavolsag:int = int(darabok[2])
        self.direktirany:bool = darabok[3] == '1'
        self.atmero:int = int(darabok[4])
        self.felfedezo_neve:str = darabok[5]
        self.felfedezes_eve:int = int(darabok[6])