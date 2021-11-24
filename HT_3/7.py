# 7. Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!

def calculator_custom(op1, op2, sign_mark):
    try:
        err_counter = 0
        op1_dig = int(op1)
        op2_dig = int(op2)
        calc_lib = {"+": op1_dig + op2_dig, "-": op1_dig - op2_dig, "*": op1_dig * op2_dig, "/": op1_dig / op2_dig}
        return f"{op1} {sign_mark} {op2} = {calc_lib[sign_mark]}", err_counter
    except ValueError:
        err_counter = 1
        return "Enter correct values!", err_counter
    except ZeroDivisionError as zero_div_err:
        err_counter = 1
        return f"Error! {zero_div_err}", err_counter


while True:
    first_num = input("Enter first number: ")
    sec_num = input("Enter second number: ")
    sign_mark = input("Enter operation (+, -, *, /): ")
    result, error_value = calculator_custom(first_num, sec_num, sign_mark)
    if error_value == 0:
        print(result)
        break
    else:
        print(result)
