# 2. Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно).

first_year = int(input("Enter first year: "))
last_year = int(input("Enter last year: "))

print("\nLeap years:\n")
for year in range(first_year, last_year+1):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year)
