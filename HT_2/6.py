# 6. Написати скрипт, який об'єднає три словника в самий перший. Оновлюється тільки перший словник.
# Дані можна "захардкодити".
#
#        Sample Dictionary :
#        dict_1 = {1:10, 2:20}
#        dict_2 = {3:30, 4:40}
#        dict_3 = {5:50, 6:60}
#        Expected Result : dict_1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


dict_1 = {5: 10, '1': 'Hello'}
dict_2 = {15: 20, '2': ', '}
dict_3 = {25: 30, '3': 'World'}
output_test = [dict_1, dict_2, dict_3]

print(f"Test input:\n{dict_1}\n{dict_2}\n{dict_3}")

dict_1.update(dict_2)
dict_1.update(dict_3)

print(f"\nResult: {dict_1}")
