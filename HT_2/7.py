# 7. Написати скрипт, який отримає максимальне і мінімальне значення із словника. Дані захардкодити.
#                Приклад словника (можете використовувати свій):
#                dict_1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#                Вихідний результат:
#                MIN: 10
#                MAX: 60

dict_1 = {1: 100, 2: 900, 3: 550, 4: 365, 5: 1, 6: 975}

print(f"Test input: {dict_1}\n")
print(f"MIN: {min(dict_1.values())}")
print(f"MAX: {max(dict_1.values())}")
