class Object:
    def __init__(self, adres: str, rodzaj: str, metry2: int, cena: float):
        self.adres = adres
        self.rodzaj = rodzaj
        self.metry2 = metry2
        self.cena = cena

    def __str__(self):
        return f'{self.adres} {self.rodzaj} {self.metry2} {self.cena}'


obj1 = Object("ul.Miła", "Mieszkanie", 30000000, 40.0)
print(obj1)

pass