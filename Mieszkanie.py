import Object
from Object import Object

class Mieszkanie:
    def __init__(self, object: Object, iloscPokoi: int, numerMieszkania: int, pietro:int):
        self.object = object
        self.iloscPokoi = iloscPokoi
        self.numerMieszkania = numerMieszkania
        self.pietro = pietro

    def __str__(self):
        return f'Mieszkanie znajduje się {self.object}:\n ' \
               f'Ilość pokoi: {self.iloscPokoi}\n ' \
               f'numer mieszkania: {self.numerMieszkania}\n ' \
               f'piętro: {self.pietro}'


mieszkanie1 = Mieszkanie(object, 3, 22,1)
print(mieszkanie1)

pass
