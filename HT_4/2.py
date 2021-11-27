# 2. Написати функцію < bank > , яка працює за наступною логікою: користувач робить вклад у розмірі
# < a > одиниць строком на
# < years > років під
# < percents > відсотків (кожен рік сума вкладу збільшується на цей відсоток, ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки).
#
# Параметр < percents > є необов'язковим і має значення по замовчуванню < 10 > (10%).
# Функція повинна принтануть і вернуть суму, яка буде на рахунку.

def bank(a, years, percents=10):
    try:
        a = float(a)
        years = int(years)
        if percents != 10:
            percents = float(percents)
        for i in range(years):
            a += a * (percents/100)
        return f"Your total funds (with percents) = {a}"
    except ValueError:
        return "Enter correct values next time :)"

test_a = input("Enter your funds: ")
test_yr = input("Period of years: ")
test_pcent = input("Enter percents (leave blank if you want): ")

if test_pcent == '':
    result = bank(test_a, test_yr)
else:
    result = bank(test_a, test_yr, test_pcent)

print(result)
