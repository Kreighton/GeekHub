# 2. Написати скрипт, який пройдеться по списку, який складається із кортежів, і замінить для кожного кортежа останнє значення.
#   Список із кортежів можна захардкодити. Значення, на яке замінюється останній елемент кортежа вводиться користувачем.
#   Значення, введене користувачем, можна ніяк не конвертувати (залишити рядком). Кількість елементів в кортежу повинна бути різна.
#             Приклад списка котежів: [(10, 20, 40), (40, 50, 60, 70), (80, 90), (1000,)]
#             Очікуваний результат, якщо введено "100":
#        Expected Output: [(10, 20, "100"), (40, 50, 60, "100"), (80, "100"), ("100",)]


def replace_last_item(old_list, replaced_item):
    for i in range(len(old_list)):
        old_list[i] = list(old_list[i])
        old_list[i][-1] = replaced_item
        old_list[i] = tuple(old_list[i])
    return old_list


tested_tuples_list = [(50, 60), ("Hello", ", ", "World"), (90, 100, 120, 150)]

replace = input("Type replacement item: ")

print(f"\nTest input: {tested_tuples_list}\n")
print(f"Result: {replace_last_item(tested_tuples_list,replace)}")
