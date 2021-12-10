"""1. Доповніть програму-банкомат з попереднього завдання таким функціоналом, як використання банкнот.
   Отже, у банкомата повинен бути такий режим як "інкассація", за допомогою якого в нього можна "загрузити" деяку кількість банкнот (вибирається номінал і кількість).
   Зняття грошей з банкомату повинно відбуватись в межах наявних банкнот за наступним алгоритмом - видається мінімальна кількість банкнот наявного номіналу. P.S. Будьте обережні з використанням "жадібного" алгоритму (коли вибирається спочатку найбільша банкнота, а потім - наступна за розміром і т.д.) - в деяких випадках він працює неправильно або не працює взагалі. Наприклад, якщо треба видати 160 грн., а в наявності є банкноти номіналом 20, 50, 100, 500,  банкомат не зможе видати суму (бо спробує видати 100 + 50 + (невідомо), а потрібно було 100 + 20 + 20 + 20 ).
   Особливості реалізації:
   - перелік купюр: 10, 20, 50, 100, 200, 500, 1000;
   - у одного користувача повинні бути права "інкасатора". Відповідно і у нього буде своє власне меню із пунктами:
     - переглянути наявні купюри;
     - змінити кількість купюр;
   - видача грошей для користувачів відбувається в межах наявних купюр;
   - якщо гроші вносяться на рахунок - НЕ ТРЕБА їх розбивати і вносити в банкомат - не ускладнюйте собі життя, та й, наскільки я розумію, банкомати все, що в нього входить, відкладає в окрему касету.
2. Для кращого засвоєння - перед написанням коду із п.1 - видаліть код для старої програми-банкомату і напишіть весь код наново (завдання на самоконтроль).
   До того ж, скоріш за все, вам прийдеться і так багато чого переписати.

   """

import json
import csv


class InsufficientBanknotes(Exception):
    pass


class InsufficientFunds(Exception):
    pass


class NegativeFunds(Exception):
    pass


class WrongOperationError(Exception):
    pass


class NoSuchBanknote(Exception):
    pass


def login_pword_check(login, pword):
    login_accepted = False
    incasation = False
    with open('users.data') as users:
        reader = json.load(users)
        for row in reader['Logins_data']:
            if [login, pword] == [row["Login"], row["Password"]]:
                login_accepted = True
                if row["Incasate"] == 'True':
                    incasation = True
    users.close()
    return login_accepted, incasation


def add_transaction(login, operation, funds):
    transaction = {operation: str(funds)}
    transaction_json = json.dumps(transaction)
    with open(f'{login}_transactions.data', 'a') as temp:
        temp.write(f'{transaction_json}\n')
        temp.close()
    return


def check_balance(login):
    with open(f'{login}_balance.data', 'r') as temp:
        user_balance = temp.read()
        temp.close()

    return f'Текущий баланс пользователя {login} = {user_balance}'


def drop_balance(login):
    # Функция заметно увеличилась :)
    print('3 - Снятие баланса')
    try:
        dropped_funds = int(input('Введите количество средств для снятия\n'
                                    'Доступные купюры: 10, 20, 50, 100, 200, 500, 1000: '))
        if dropped_funds < 0:
            raise NegativeFunds()
        user_funds = int(open(f'{login}_balance.data', 'r').read())
        if dropped_funds > user_funds:
            raise InsufficientFunds()

        # Банкноты, подтянутые из файла
        total_banknotes = {}

        # Банкноты, которые будут подсчитыватся для вывода пользователю. Все начинают с 0, в дальнейшем выведутся
        # все, которые не 0
        dropped_banknotes = {10: 0, 20: 0, 50: 0, 100: 0, 200: 0, 500: 0, 1000: 0}

        # Вытягиваем банкноты из файла в дикт
        with open('incasator_funds.data', 'r') as temp:
            reader = json.load(temp)
            for row in reader:
                total_banknotes[int(row)] = int(reader[row])
            temp.close()

        # Сразу проверка, ошибка если сумма всех банкнот меньше суммы, затребованой пользователем
        if dropped_funds > sum([key * total_banknotes[key] for key in total_banknotes]):
            raise InsufficientBanknotes

        dropped_funds_local = dropped_funds
        funds_avaliable_in_banknotes = 0

        # Основной цикл для проверки, можно ли снять по присутствующим в файле банкнотам нужную сумму
        while True:
            # Счётчик неудачных попыток отнять банкноту для суммы.
            # Если = 7, ошибка "недостаточно банкнот"
            failed_drop = 0
            for banknote in sorted(total_banknotes.keys(), reverse=True):
                if dropped_funds_local // int(banknote) > 0 and int(total_banknotes[banknote]) > 0:
                    # Убираем одну банкноту из дикта
                    total_banknotes[banknote] = int(total_banknotes[banknote]) - 1
                    # Добавляем банкноту в дикт для вывода
                    dropped_banknotes[banknote] += 1
                    # Сумма средств для проверки сходства с запрошенной суммой
                    funds_avaliable_in_banknotes += int(banknote)
                    # Локальная переменная запрошенной суммы для вычитания
                    # Способствует завершению цикла while, если она <10
                    dropped_funds_local -= int(banknote)
                else:
                    failed_drop += 1
            if funds_avaliable_in_banknotes != dropped_funds and failed_drop == 7:
                raise InsufficientBanknotes()
            if dropped_funds_local < 10:
                break
        # Вносим изменения в файл, хранящий банкноты
        with open('incasator_funds.data', 'w') as temp:
            temp.write(json.dumps(total_banknotes))
            temp.close()
        # Вносим изменения в баланс
        with open(f'{login}_balance.data', 'w') as temp:
                temp.write(str(user_funds - dropped_funds))
                temp.close()
        # Добавляем транзакцию
        add_transaction(login, 'drop', dropped_funds)
        result = ''
        for key in dropped_banknotes.keys():
            if dropped_banknotes[key] > 0:
                result += f'\n{dropped_banknotes[key]} банкнот по {key}'
        return f'Поздравляем! Со счёта пользователя {login} было снято {dropped_funds} у.е.{result}'

    except NegativeFunds:
        return 'Вы ввели некорректную сумму! Возврат в главное меню'
    except ValueError:
        return 'Вы ввели некорректную сумму! Возврат в главное меню'
    except InsufficientFunds:
        return 'Недостаточно средств! Возврат в главное меню'
    except InsufficientBanknotes:
        return 'В банкомате недостаточно средств! Возврат в главное меню'


def add_balance(login):
    print('2 - Пополнение баланса')
    try:
        additional_funds = float(input('Введите количество средств для пополнения: '))
        if additional_funds < 0:
            raise NegativeFunds()
        else:
            user_funds = float(open(f'{login}_balance.data', 'r').read())
            with open(f'{login}_balance.data', 'w') as temp:
                temp.write(str(user_funds + additional_funds))
                temp.close()
            add_transaction(login, 'add', additional_funds)
            return f'Поздравляем! Счёт пользователя {login} был пополнен на {additional_funds} у.е'

    except NegativeFunds:
        return 'Вы ввели некорректную сумму! Возврат в главное меню'
    except ValueError:
        return 'Вы ввели буквы! Возврат в главное меню'


def check_bankomat_funds():
    result = ''
    with open('incasator_funds.data', 'r') as temp:
        reader = json.load(temp)
        for row in reader:
            result += f'Количество купюр {row} = {reader[row]}\n'
        temp.close()
    return result


def add_bankomat_funds():
    banknotes = {}
    print('2 - Изменить кол-во купюр в банкомате')
    try:
        banknotes_value = input('Введите купюру: ')
        banknotes_num = input('Введите количество купюр: ')
        if banknotes_num.isdigit() and banknotes_value.isdigit():
            if int(banknotes_num) < 0:
                raise NegativeFunds()
            else:
                with open('incasator_funds.data', 'r') as temp:
                    reader = json.load(temp)
                    for row in reader:
                        banknotes[row] = reader[row]
                    temp.close()
                if banknotes_value in banknotes.keys():
                    banknotes[banknotes_value] = banknotes_num
                    with open('incasator_funds.data', 'w') as temp:
                        temp.write(json.dumps(banknotes))
                        temp.close()
                    return f'Вы изменили кол-во банкнот {banknotes_value} на {banknotes_num} штук'
                else:
                    raise NoSuchBanknote()
        else:
            raise ValueError()
    except NegativeFunds:
        return 'Вы ввели некорректную сумму! Возврат в главное меню'
    except ValueError:
        return 'Вы ввели буквы! Возврат в главное меню'
    except NoSuchBanknote:
        return 'Такой банкноты не существует! Возврат в главное меню'


def start(login, incasator=False):
    try:
        while True:
            if not incasator:
                user_operation = int(input(f'{"-" * 30}\nДобро пожаловать, {login}! Выберите операцию:'
                                           '\n1. Просмотреть баланс'
                                           '\n2. Пополнение баланса'
                                           '\n3. Снятие баланса'
                                           '\n4. Выход\n'))
                if user_operation in range(1, 5):
                    if user_operation == 1:
                        print(f'{"-" * 30}\n{check_balance(login)}')
                    elif user_operation == 2:
                        print(f'{"-" * 30}\n{add_balance(login)}')
                    elif user_operation == 3:
                        print(f'{"-" * 30}\n{drop_balance(login)}')
                    elif user_operation == 4:
                        print('4 - Выход')
                        return
                else:
                    raise WrongOperationError()
            else:
                print(f'{"-" * 40}\nПриветствую, {login} (инкасатор) Выберите операцию!')
                incas_operation = int(input('1. Проверить наличие купюр\n'
                                            '2. Изменить кол-во купюр в банкомате\n'
                                            '3. Выход\n'))
                if incas_operation in range(1, 4):
                    if incas_operation == 1:
                        print(f'{"-" * 40}\n{check_bankomat_funds()}')
                    if incas_operation == 2:
                        print(f'{"-" * 40}\n{add_bankomat_funds()}')
                    if incas_operation == 3:
                        print('3 - Выход')
                        return
                else:
                    raise WrongOperationError()

    except ValueError:
        return 'error'
    except WrongOperationError:
        return 'Введите правильный номер операции!'




try_counter = 3

# Pavel, 123 - customer
# James, asd - incasator

while True:
    if try_counter == 0:
        print(f'{"-" * 30}\nВы исчерпали 3 попытки! Закрытие программы.')
        break
    custom_login = input(f'{"-" * 30}\nВведите логин: ')
    custom_password = input('Введите пароль: ')
    access, incasator = login_pword_check(custom_login, custom_password)
    if access:
        start(custom_login, incasator)
        break
    else:
        try_counter -= 1
        print(f'{"-" * 30}\nОшибка ввода логина/пароля. Осталось {try_counter} попыток')
