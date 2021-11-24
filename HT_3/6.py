# 6. Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
#   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
# -  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
# -  якщо довжина бульше 50 - > ваша фантазiя

from string import ascii_letters


def smallstring(input_string):
    only_letters = ''
    only_nums_sum = 0
    for i in input_string:
        if i in ascii_letters:
            only_letters += i
        elif i.isdigit():
            only_nums_sum += int(i)
    return f"Sum of numbers from string = {only_nums_sum}\nString with only letters = {only_letters}"


def mediumstring(input_string):
    number_of_digits = 0
    number_of_letters = 0
    for i in input_string:
        if i.isdigit():
            number_of_digits += 1
        else:
            number_of_letters += 1
    return f"String length = {len(input_string)}\nDigits in string = {number_of_digits}\nLetters in string = {number_of_letters}"


def largestring_custom(input_string):
    input_list = [i for i in input_string]
    input_list.sort()
    result_string = ''
    count = 0
    for i in range(len(input_list)):
        try:
            if input_list[i] == input_list[i + 1]:
                count += 1
            else:
                result_string += f'Number of \'{input_list[i]}\' symbol in list = {count}\n'
                count = 0
        except:
            return result_string


def length_cases(input_string):
    string_len = len(input_string)

    if string_len > 50:
        return largestring_custom(input_string)
    elif string_len < 30:
        return smallstring(input_string)
    else:
        return mediumstring(input_string)


test_input = input("Enter the string:")

print(length_cases(test_input))
