# 7. Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!

def calculator_custom(op1, op2, sign_mark):
    try:
        op1_dig = int(op1)
        op2_dig = int(op2)
        calc_lib = {"+": op1_dig + op2_dig, "-": op1_dig - op2_dig, "*": op1_dig * op2_dig, "/": op1_dig / op2_dig}
        return f"{op1} {sign_mark} {op2} = {calc_lib[sign_mark]}"
    except:
        return "Enter correct values!"


while True:
    first_num = input("Enter first number: ")
    sec_num = input("Enter second number: ")
    sign_mark = input("Enter operation (+, -, *, /): ")
    result = calculator_custom(first_num, sec_num, sign_mark)
    if result != "Enter correct values!":
        print(result)
        break
    else:
        print(result)
