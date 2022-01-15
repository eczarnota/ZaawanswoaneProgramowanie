from Object import Object
from Developer import Developer


class Zamowienie:
    def __init__(self, numerZamowienia: int, listaObiektow: Object, wartoscZamowienia: float, developer: Developer):
        self.numerZamowienia = numerZamowienia
        self.listaObiektow = listaObiektow
        self.wartoscZamowienia = wartoscZamowienia
        self.developer = developer

    def __str__(self):
        return f'Zamowienie o numerze {self.numer_zamowienia}:\n ' \
               f'Zamowione obiekty: {self.lista_obiektow}\n ' \
               f'Wartosc zamowienia: {self.wartosc_zamowienia}\n ' \
               f'Developer obsługujący zamowienie: {self.developer}'


pass
