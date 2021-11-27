# 4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона, і вертатиме список простих чисел всередині цього діапазона.


from math import factorial


def prime_list(l_start, l_end):
    err_checker = 0
    result_list = []
    try:
        if int(l_start) < int(l_end):
            for digits in range(int(l_start), int(l_end)+1):
                if (factorial(digits - 1) + 1) % digits == 0:
                    result_list.append(digits)
            return result_list, err_checker
        else:
            err_checker = 1
            return "Error. First value cannot be bigger than second value.", err_checker
    except ValueError as e:
        err_checker = 1
        return "Error. Please enter correct values.", err_checker


while True:
    test_digits = list(input("Enter two digits, separated by spaces. Second digit must be bigger: ").split(" "))
    result, err = prime_list(test_digits[0], test_digits[1])
    print(result)
    if err == 0:
        break
