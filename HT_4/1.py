# 1. Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата,
# і вертатиме 3 значення (кортеж): периметр квадрата, площа квадрата та його діагональ.


from math import sqrt


def square(sqr_side):
    error_counter = 0
    try:
        sqr_side = int(sqr_side)
        sqr_result = (sqr_side * 4, sqr_side * 2, sqrt(2 * (sqr_side ** 2)))
        return f'P, S, d = {sqr_result}', error_counter
    except ValueError:
        error_counter = 1
        return 'Enter correct input value!', error_counter


while True:
    test_input = input("Enter value: ")
    result, err = square(test_input)
    print(result)
    if err == 0:
        break
