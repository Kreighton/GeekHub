# 3. Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000, и яка вертатиме True, якщо це число просте, и False - якщо ні.

from math import factorial


def is_prime(digit):
    err_checker = 0
    try:
        digit = int(digit)
        if 0 < digit <= 1000:
            if (factorial(digit - 1) + 1) % digit == 0:
                return True, err_checker
            else:
                return False, err_checker
    except ValueError:
        err_checker = 1
        return 'Error, enter correct value!', err_checker


while True:
    test_digit = input("Enter random digit: ")
    result, err = is_prime(test_digit)
    print(result)
    if err == 0:
        break
