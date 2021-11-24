# 4. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат.
# Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, обробляє повернутий ними результат та також повертає результат.
# Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3


def simple_1(test_str):
    digit_list = []
    letter_list = []
    for i in test_str:
        if i.isdigit():
            digit_list.append(i)
        else:
            letter_list.append(i)

    return digit_list, letter_list


def simple_2(digit_s):
    digit_s = list(map(int,digit_s))
    result = f'\nMax digit in string = {max(digit_s)}\nMin digit in string = {min(digit_s)}' \
             f'\nSum of digits in string = {sum(digit_s)}'

    return result


def simple_3(letter_s):
    letter_s.sort()
    letter_s_string = ''.join(letter_s)
    result = f'\nSorted letter is list: {letter_s_string}'

    return result

def simpliest_functions(test_str):
    result = ''
    list_of_strings = [i for i in test_str]
    digit_list, letter_list = simple_1(list_of_strings)
    result += simple_2(digit_list)
    result += simple_3(letter_list)
    return result


test_input = input('Enter your string: ')

print(simpliest_functions(test_input))
