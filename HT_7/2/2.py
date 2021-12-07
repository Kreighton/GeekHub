# 2. Написати функцію, яка приймає два параметри: ім'я файлу та кількість символів.
#   На екран повинен вивестись список із трьома блоками - символи з початку, із середини та з кінця файлу.
#   Кількість символів в блоках - та, яка введена в другому параметрі.
#   Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша, ніж є в файлі (наприклад, файл із двох символів і треба вивести по одному символу, то що виводити на місці середнього блоку символів?)
#   В репозиторій додайте і ті файли, по яким робили тести.
#   Як визначати середину файлу (з якої брать необхідні символи) - кількість символів поділити навпіл, а отримане "вікно" символів відцентрувати щодо середини файла і взяти необхідну кількість. В разі необхідності заокруглення одного чи обох параметрів - дивіться на свій розсуд.
#   Наприклад:
#   █ █ █ ░ ░ ░ ░ ░ █ █ █ ░ ░ ░ ░ ░ █ █ █    - правильно
#                     ⏫ центр
#   █ █ █ ░ ░ ░ ░ ░ ░ █ █ █ ░ ░ ░ ░ █ █ █    - неправильно

class TooMuchToCenter(Exception):
    pass


def func(text_file, syms):
    try:
        with open(text_file, 'r') as temp:
            txt_file = temp.read()
            temp.close()
        a = [[i for i in txt_file], []]
        file_len = len(txt_file)
        if syms >= file_len:
            raise TooMuchToCenter()
        mid_symbol = file_len // 2
        for i in range(file_len):
            if i < syms or i >= file_len - syms or i in range(mid_symbol - (syms // 2), mid_symbol + (syms - (syms // 2))):
                a[1].append('█')
            else:
                a[1].append('░')
        result = ' '.join(a[0]) + '\n' + ' '.join(a[1]) + '\n'
        return f'{result}\n{(" " * (len(" ".join(a[1])) // 2)) + "⏫ центр"}'
    except TooMuchToCenter:
        return 'Error, The entered value is very big!'

try:
    user_input = int(input("Enter value: "))
    user_test = int(input("Enter test txt file number (0-2): "))
    if user_test not in range(0, 3):
        raise ValueError()
    print(func(f'test_{user_test}.txt', user_input))
except ValueError:
    print("ERROR! Enter correct value!")



