from random import randint

# exercise 1:
def scan_number(first_number, second_number):
    if second_number > first_number:
        print('Привет')
    
# exercise 2:
def scan_name(list, name_search):
    if name_search in list:
        print(f'Привет, {name_search}')
    else:
        print('Нет такого имени')

# exercise 3:
# generating a random list:
def first_list(number):
    list = []
    for i in range(number):
        list.append(randint(-10, 10))
    return list

# or handwriting:
# def first_list(number):
#     list = []
#     for i in range(number):
#         list.append(int(input(f'{i + 1} Число: ')))
#     return list

def multiples_element(list, multiples):
    new_list = []
    for value in list:
        if value % multiples == 0 and value != 0:
            new_list.append(value)
    return new_list

# exercise 1:
given_number = 7
compared_number = int(input('\nВведите число: '))
scan_number(given_number, compared_number)

# exercise 2:
name_list = ['Вячеслав']
search_name = input('\nВведите имя для поиска: ')
scan_name(name_list, search_name)

# exercise 3:
multiples_number = 3
number_element = int(input('\nКоличество чисел в массиве: '))
first_array = first_list(number_element)
print(f'\nИзначальный список: {first_array}')
print(f'Элементы массива кратные {multiples_number}: {multiples_element(first_array, multiples_number)}')


# Текстовая задача

# [((())()(())]]

# последовательность выше не является правильной

# изменения чтобы считать правильной, нужно заменить предпоследнюю скобку:

# [((())()(()))]