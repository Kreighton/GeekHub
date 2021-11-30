#7. Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну послідовність (рядок, список, кортеж) і повертає генератор, який буде вертати значення з цієї послідовності, при цьому, якщо було повернено останній елемент із послідовності - ітерація починається знову.
#   Приклад (якщо запустили його у себе - натисніть Ctrl+C ;) ):
#   >>>for elem in generator([1, 2, 3]):
#   ...    print(elem)
#   ...
#   1
#   2
#   3
#   1
#   2
#   3
#   1
#   .......

def generator(val):
    item = 0
    while True:
        if item == len(val)-1:
            item = 0
        else:
            item += 1
        yield val[item]


test_list = input('Enter custom string: ')
to_list = input('Convert to list? (y/n): ')
to_tuple = input('Convert to tuple? (y/n): ')

if to_list == 'y':
    test_list = [val for val in test_list]

if to_tuple == 'y':
    test_list = tuple(val for val in test_list)

for elem in generator(test_list):
    print(elem)
