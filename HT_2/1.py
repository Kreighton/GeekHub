# 1. Написати скрипт, який конкатенує всі елементи в списку і виведе їх на екран. Список можна "захардкодити".
#   Елементами списку повинні бути як рядки, так і числа.

listOfStrings = ["Print", " ", "theese", " ", 7, " ", "elements", 10]

print(f"Test list = {listOfStrings}")
print(f"String of concatenated elements: {''.join(map(str,listOfStrings))}")
