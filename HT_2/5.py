# 5. Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями (дублікати значень - видалити).
# Словник для роботи захардкодити свій.
#                Приклад словника (не використовувати):
#                {'a': 1, 'b': 3, 'c': 1, 'd': 5}
#                Очікуваний результат:
#                {'a': 1, 'b': 3, 'd': 5}


dict_1 = {'key1': 123, 'key2': 124, 'key3': 123, 'key4': 125}
dict_new = {}

for key, val in dict_1.items():
    if val not in dict_new.values():
        dict_new[key] = val

print(f"Test dictionary input: {dict_1}\n")
print(f"Result = {dict_new}")
