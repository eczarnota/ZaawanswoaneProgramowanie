class Developer:

    def __init__(self, name: str, surname: str, buildings: int, price: int):
        self.name = name
        self.surname = surname
        self.buildings = buildings
        self.price = price

    def __str__(self):
        return f"Developer {self.name} {self.surname}"


dev1 = Developer("Marek", "Nowak", 1, 3000000)
print(dev1)

pass
