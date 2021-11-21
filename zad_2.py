class Liblary:
    def __init__(self, city: str, street: str, zip_code: int, open_hours: str, phone: int):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Biblioteka znajduje się pod adresem:  {self.city} ul.{self.street}, {self.zip_code}. Godziny otwarcia: {self.open_hours}, telefon kontaktowy: {self.phone}'
    pass

class Order:
    def __init__(self, employee: str, student: str, books: str, order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Zamówienie obejmójące: {self.books}, przygotowane w dniu: {self.order_date} przez: {self.emplpoyee}, dla: {self.student}'

    pass

class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: str, birth_date: str,
                 city: str, street: str, zip_code: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'Informacje o pracowniku {self.first_name} {self.last_name}: Informacje o pracowniku: : Data zatrudnienia:{self.hire_date} :\n Data urdzenia: {self.birth_date} : Dane zamieszkania: Misto: {self.city}, ulica: {self.street} {self.zip_code}.: Numer kontaktowy: {self.phone}'

    pass

class Book:
    def __init__(self, library: str, publication_date: str,
                 author_name: str, author_surname: str, number_of_pages: str):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Biblioteka: {self.library},:\n Data publikacji:{self.publication_date} :\n Dane autora: {self.author_name}{self.author_surname} :\n Ilość stron:{self.number_of_pages}'
    pass