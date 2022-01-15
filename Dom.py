from Object import Object

class Dom:
    def __init__(self, adres: str, ilośćPokoi: int, wielkoscDzialki: int, pietra: int):
        self.adres = adres
        self.ilośćPokoi = ilośćPokoi
        self.wielkoscDzialki = wielkoscDzialki
        self.pietra = pietra

    def __str__(self):
        return f'Dom znajduje się {self.object}:\n ' \
               f'Ilość pokoi: {self.ilośćPokoi}\n ' \
               f'wielkoscDzialki: {self.wielkoscDzialki}\n ' \
               f'ilosc pięter: {self.pietra}'


pass
