# 7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.


def same_symbols(test_string):
    input_list = [str_items for str_items in test_string]
    output_dict = {unique_items: input_list.count(unique_items) for unique_items in test_string}
    result = ''
    for keys in output_dict:
        result += f'Number of \'{keys}\' symbol in list = {output_dict[keys]}\n'
    return result

test_input = input("Enter the string:")
print(same_symbols(test_input))
