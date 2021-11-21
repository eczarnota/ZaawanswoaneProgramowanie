def count(lista1: list, lista2: list) -> list:
    lista3 = lista1 + lista2
    set(lista3)
    list4 = []
    for element in lista3:
        list4.append(element**3)
    return list4
lista_nr_1 = [1,2,5,6,7]
lista_nr_2 = [1,3,4,8,7]
print(count(lista_nr_1, lista_nr_2))