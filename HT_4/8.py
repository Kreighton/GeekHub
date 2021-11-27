# 8. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку. Тобто, функція приймає два аргументи: список і величину зсуву (якщо ця величина додатня - пересуваємо з кінця на початок, якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
#   Наприклад:
#       fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
#       fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]


def list_shift(test_list, shift_val):
    err = 0
    try:
        shift_val = int(shift_val)
        if shift_val < 0:
            shift_val = len(test_list) + shift_val
        for i in range(shift_val):
            test_list.insert(0, test_list.pop())
        return f"Result = {test_list}", err
    except ValueError:
        return 'Error, enter correct value!', err


user_list = [1, 2, 3, 4, 5]

print(f'Your test list = {user_list}')

while True:
    test_shift_val = input("Enter shift value: ")
    result, err_counter = list_shift(user_list, test_shift_val)
    print(result)
    if err_counter == 0:
        break
