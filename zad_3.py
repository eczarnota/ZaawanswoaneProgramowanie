def even(number1: int) -> bool:
    if number1%2==0:
        return True
    else:
        return False
zmienna = even(4)

if zmienna == True:
    print('Liczba parzysta')
else:
    print('Liczba nieparzysta')

