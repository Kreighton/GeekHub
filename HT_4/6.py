# 6. Вводиться число. Якщо це число додатне, знайти його квадрат, якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.


def change_the_number(test_digit):
    try:
        test_digit = int(test_digit)
        result_dict = {1: test_digit ** 2, 2: test_digit + 100}
        if test_digit > 0:
            return f'Result = {result_dict[1]}'
        elif test_digit < 0:
            return f'Result = {result_dict[2]}'
        else:
            return f'Result = {test_digit}'
    except ValueError:
        return 'Enter correct value!'


test_input = input('Enter test value: ')
print(change_the_number(test_input))
