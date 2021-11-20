numbers = [5, 10, 15, 20, 25]
numbers_i = []

def number_i(numbers):
    for number in numbers:
        number *= 2
        numbers_i.append(number)
    return numbers_i

def number_ii(numbers):
    numbers_ii = [number * 2 for number in numbers]
    return numbers_ii

#print(number_i(numbers))
#print(number_ii(numbers))