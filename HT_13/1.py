#1. Створити клас Calc, який буде мати атребут last_result та 4 метод
# Методи повинні виконувати математичні операції з 2-ма числами, а саме
# додавання, віднімання, множення, ділення.
# - Якщо під час створення екземпляру класу звернутися до атребута
# last_result він повинен повернути пусте значення
# - Якщо використати один з методів - last_result повенен повернути
# результат виконання попереднього методу.
#   - Додати документування в клас (можете почитати цю статтю: h://realpython.com/documenting-python-code/ )

class Calc(object):
    last_result = ''
    
    def sum_digits(self, a, b):
        self.last_result = a + b
    def minus_digits(self, a, b):
        self.last_result = a - b
    def multiple_digits(self, a, b):
        self.last_result = a * b
    def divide_digits(self, a, b):
        self.last_result = a / b
        
        
calc_1 = Calc()
calc_2 = Calc()
calc_3 = Calc()
calc_4 = Calc()

calc_1.sum_digits(2, 2)
print(calc_1.last_result)

calc_2.minus_digits(4, 2)
print(calc_2.last_result)

calc_3.multiple_digits(5, 2)
print(calc_3.last_result)

calc_4.divide_digits(100, 10)
print(calc_4.last_result)

