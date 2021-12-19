"""1. Доповніть програму-банкомат наступним функціоналом:
   - новий пункт меню, який буде виводити поточний курс валют (API Приватбанк)
2. Написати скрипт, який буде приймати від користувача назву валюти і початкову дату.
   - Перелік валют краще принтануть.
   - Також не забудьте указати, в якому форматі коритувач повинен ввести дату.
   - Додайте перевірку, чи введена дата не знаходиться у майбутньому ;)
   - Також перевірте, чи введена правильна валюта.
   Виконуючи запроси до API архіву курсу валют Приватбанку, вивести інформацію про зміну
   курсу обраної валюти (Нацбанк) від введеної дати до поточної. Приблизний вивід наступний:
   Currency: USD
   Date: 12.12.2021
   NBU:  27.1013   -------
   Date: 13.12.2021
   NBU:  27.0241   -0,0772
   Date: 14.12.2021
   NBU:  26.8846   -0,1395
3. Конвертер валют. Прийматиме від користувача назву двох валют і суму (для першої).
   Робить запрос до API архіву курсу валют Приватбанку (на поточну дату) і виконує
   конвертацію введеної суми з однієї валюти в іншу.
P.S. Не забувайте про файл requirements.txt
P.P.S. Не треба сходу ДДОСить Приватбанк - додайте хоча б по 0.5 секунди між запросами.
       Хоч у них і не написано за троттлінг, але будьмо чемними ;)
Інформація для виконання:
- документація API Приватбанка:
  - архів курсів: https://api.privatbank.ua/#p24/exchangeArchive
  - поточний курс: https://api.privatbank.ua/#p24/exchange
- інформація про використання форматування дати в Python: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
- модуль requests: https://docs.python-requests.org/en/latest/

   """

import json
import csv
import sqlite3
import requests
from datetime import date, timedelta, datetime
import time


class WrongDateInput(Exception):
    pass
class CurrencyNotExists(Exception):
        pass

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

#done
def login_pword_check(login, pword):
    login_accepted = False
    incasation = False
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    is_account_exists = cur.execute('select is_incasator from user_logs where user_login=? and user_password=?', (login, pword)).fetchone()
    con.close()
    if is_account_exists:
        login_accepted = True
        if is_account_exists[0] == 1:
            incasation = True
    return login_accepted, incasation

#done
def add_transaction(login, operation, funds):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute(f'insert into {login}_transactions(operation, funds) values(?, ?)', (operation, funds))
    con.commit()
    con.close()
    return

#done
def check_balance(login):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    user_id = cur.execute('select id from user_logs where user_login=?', (login,)).fetchone()
    user_balance = cur.execute('select user_balance from balance where id=?', (user_id[0],)).fetchone()
    con.close()
    return f'Текущий баланс пользователя {login} = {user_balance[0]}'


def drop_balance(login):
    print('3 - Снятие баланса')
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    try:
        # Вытягиваем банкноты из таблицы
        total_banknotes = cur.execute('SELECT banknote_value, banknote_total FROM banknotes').fetchall()
        total_banknotes_dict = {total_banknotes[i][0]: total_banknotes[i][1] for i in range(len(total_banknotes))}
        print(f'{"-" * 40}\nДоступное количество купюр:')
        print('\n'.join(f'{key} = {total_banknotes_dict[key]}' for key in total_banknotes_dict))
        dropped_funds = int(input('Введите количество средств для снятия: '))


        user_id = cur.execute('select id from user_logs where user_login=?', (login,)).fetchone()
        user_funds = cur.execute('select user_balance from balance where id=?', (user_id[0],)).fetchone()[0]
        if dropped_funds < 0:
            raise NegativeFunds()
        if dropped_funds > user_funds:
            raise InsufficientFunds()


        # Банкноты, которые будут подсчитыватся для вывода пользователю. Все начинают с 0, в дальнейшем выведутся
        # все, которые не 0
        dropped_banknotes = {10: 0, 20: 0, 50: 0, 100: 0, 200: 0, 500: 0, 1000: 0}

        # Сразу проверка, ошибка если сумма всех банкнот меньше суммы, затребованой пользователем
        if dropped_funds > sum([total_banknotes[i][0] * total_banknotes[i][1] for i in range(len(total_banknotes))]):
            raise InsufficientBanknotes

        dropped_funds_local = dropped_funds
        funds_avaliable_in_banknotes = 0

        # Основной цикл для проверки, можно ли снять по присутствующим в файле банкнотам нужную сумму
        while True:
            # Счётчик неудачных попыток отнять банкноту для суммы.
            # Если = 7, ошибка "недостаточно банкнот"
            failed_drop = 0
            for banknote in sorted(total_banknotes_dict.keys(), reverse=True):
                if dropped_funds_local // int(banknote) > 0 and int(total_banknotes_dict[banknote]) > 0:
                    # Убираем одну банкноту из дикта
                    total_banknotes_dict[banknote] -= 1
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
        total_banknotes = [(total_banknotes_dict[key], key) for key in total_banknotes_dict]
        cur.executemany('UPDATE banknotes SET banknote_total=? WHERE banknote_value=?', total_banknotes)

        # Вносим изменения в баланс
        user_id = cur.execute('select id from user_logs where user_login=?', (login,)).fetchone()
        user_funds = cur.execute('select user_balance from balance where id=?', (user_id[0],)).fetchone()
        cur.execute('UPDATE balance SET user_balance=? WHERE id=?', (user_funds[0] - dropped_funds, user_id[0]))
        con.commit()
        con.close()

        # Добавляем транзакцию
        add_transaction(login, 'drop', dropped_funds)
        result = ''
        for key in dropped_banknotes.keys():
            if dropped_banknotes[key] > 0:
                result += f'\n{dropped_banknotes[key]} банкнот по {key}'
        return f'Поздравляем! Со счёта пользователя {login} было снято {dropped_funds} у.е.{result}'

    except NegativeFunds:
        return 'Вы ввели некорректную сумму! Возврат в главное меню'
    except InsufficientFunds:
        return 'Недостаточно средств! Возврат в главное меню'
    except ValueError:
        return 'Ошибка ввода! Возврат в главное меню'
    except InsufficientBanknotes:
        return 'В банкомате недостаточно средств! Возврат в главное меню'

#done
def add_balance(login):
    print('2 - Пополнение баланса')
    try:
        additional_funds = float(input('Введите количество средств для пополнения: '))
        if additional_funds < 0:
            raise NegativeFunds()
        else:
            con = sqlite3.connect('users.db')
            cur = con.cursor()
            user_id = cur.execute('select id from user_logs where user_login=?', (login,)).fetchone()
            user_funds = cur.execute('select user_balance from balance where id=?', (user_id[0],)).fetchone()
            cur.execute('UPDATE balance SET user_balance=? WHERE id=?', (user_funds[0] + additional_funds, user_id[0]))
            con.commit()
            con.close()
            add_transaction(login, 'add', additional_funds)
            return f'Поздравляем! Счёт пользователя {login} был пополнен на {additional_funds} у.е'

    except NegativeFunds:
        return 'Вы ввели некорректную сумму! Возврат в главное меню'
    except ValueError:
        return 'Вы ввели буквы! Возврат в главное меню'

#done
def check_bankomat_funds():
    result = ''
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    total_banknotes = cur.execute('select banknote_value, banknote_total from banknotes').fetchall()
    con.close()
    for banknote in total_banknotes:
        result += f'Количество банкнот {banknote[0]} = {banknote[1]}\n'
    return result

#done
def add_bankomat_funds():
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    print('2 - Изменить кол-во купюр в банкомате')
    try:
        banknotes_value = int(input('Введите купюру: '))
        banknotes_num = int(input('Введите количество купюр: '))
        if banknotes_num < 0:
            raise NegativeFunds()
        else:
            current_banknotes_total = cur.execute('SELECT banknote_total FROM banknotes WHERE banknote_value=?', (banknotes_value,)).fetchone()
            if current_banknotes_total:
                cur.execute('UPDATE banknotes SET banknote_total=? WHERE banknote_value=?', (banknotes_num, banknotes_value))
                con.commit()
                con.close()
                return f'Вы изменили кол-во банкнот {banknotes_value} на {banknotes_num} штук'
            else:
                raise NoSuchBanknote()
    except NegativeFunds:
        return 'Вы ввели некорректную сумму! Возврат в главное меню'
    except ValueError:
        return 'Ошибка ввода! Возврат в главное меню'
    except NoSuchBanknote:
        return 'Такой банкноты не существует! Возврат в главное меню'


def daterange(custom_date):
    for i in range(int((date.today() - custom_date).days) + 1):
        yield custom_date + timedelta(i)


def getcurrency_history(custom_date, currency):
    currencies = ['USD', 'EUR', 'RUR', 'CHF', 'GBP', 'PLZ', 'SEK', 'XAU', 'CAD']
    try:
        if currency not in currencies:
            raise CurrencyNotExists()
        dd = int(custom_date[0:2])
        mm = int(custom_date[3:5])
        yyyy = int(custom_date[6:])
        if date(yyyy, mm, dd) > date.today():
            raise WrongDateInput()
        print(f'Currency: {currency}')
        for i in daterange(date(yyyy, mm, dd)):
            time.sleep(1)
            url = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={i.strftime("%d.%m.%Y")}'
            currency_hist_data = requests.get(url=url).json()['exchangeRate']
            print(f'Date: {i.strftime("%d.%m.%Y")}')
            if i == date.today():
                print(''.join([f'NBU:    {currency_hist_data[cur]["saleRateNB"]}    -------\n'
                           for cur in range(1, len(currency_hist_data)) if currency_hist_data[cur]["currency"] == currency]))

            else:
                print(''.join([f'NBU:    {currency_hist_data[cur]["saleRateNB"]}    {float(currency_hist_data[cur]["purchaseRateNB"] - currency_hist_data[cur]["saleRateNB"])}\n'
                           for cur in range(1, len(currency_hist_data)) if currency_hist_data[cur]["currency"] == currency]))
        return 'Done!'
    except CurrencyNotExists:
        return 'Такой валюты не существует! Возврат в главное меню.'
    except WrongDateInput:
        return 'Неверно введенная дата! Возврат в главное меню'
    except ValueError:
        return 'Неверно введенная дата! Возврат в главное меню'


def curr_converter(curr_from, curr_to, curr_value):
    try:
        converted_value = 0
        curr_value = float(curr_value)
        result = 0
        func_currency = ''
        move_hist = ''
        move = ''
        curs_for_sale = ['USD', 'EUR', 'RUR']
        if curr_from == curr_to:
            result = curr_value
        elif curr_from in curs_for_sale and curr_to == 'UAH':
            move = 'sale'
            move_hist = 'saleRateNB'
            func_currency = curr_from
        elif curr_from == 'UAH' and curr_to in curs_for_sale:
            move = 'buy'
            move_hist = 'purchaseRateNB'
            func_currency = curr_to
        else:
            raise CurrencyNotExists()
        if move:
            url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
            temp = requests.get(url=url).json()
            converted_value = float([temp[i][move] for i in range(len(temp)) if temp[i]['ccy'] == func_currency][0])
            if converted_value == 0:
                yesterdays_date = (date.today() - timedelta(days=1)).strftime("%d.%m.%Y")
                url = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={yesterdays_date}'
                temp = requests.get(url=url).json()['exchangeRate']
                converted_value = float([temp[i][move_hist] for i in range(1, len(temp)) if temp[i]['currency'] == func_currency][0])
            if move == 'buy':
                result = curr_value / converted_value
            else:
                result = curr_value * converted_value
        return f"{curr_value} {curr_from} в {curr_to} = {result} {curr_to}"
    except CurrencyNotExists:
        return 'Вы ввели неверную валюту! Возврат в главное меню.'
    except ValueError:
        return 'Введеная неверная валюта или сумма для обмена! Возврат в главное меню.'


def getcurrency_current():
    url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    a = requests.get(url=url).json()
    for i in range(len(a)):
        a[i]["buy"] = "%.2f" % float(a[i]["buy"])
        a[i]["sale"] = "%.2f" % float(a[i]["sale"])
    result = ''.join([f'{a[i]["ccy"]} к {a[i]["base_ccy"]}:\nПродажа: {a[i]["buy"]}\nПокупка: '
                      f'{a[i]["sale"]}\n{"-" * 40}\n' for i in range(len(a))])
    return result


def start(login, incasator=False):
    try:
        print("-" * 30)
        while True:
            if not incasator:
                user_operation = int(input(f'Добро пожаловать, {login}! Выберите операцию:'
                                           '\n1. Просмотреть баланс'
                                           '\n2. Пополнение баланса'
                                           '\n3. Снятие баланса'
                                           '\n4. Курс валют'
                                           '\n5. Проверить историю курса валют'
                                           '\n6. Конвертер валют'
                                           '\n7. Выход\n'))
                if user_operation in range(1, 8):
                    if user_operation == 1:
                        print(f'{"-" * 30}\n{check_balance(login)}')
                    elif user_operation == 2:
                        print(f'{"-" * 30}\n{add_balance(login)}')
                    elif user_operation == 3:
                        print(f'{"-" * 30}\n{drop_balance(login)}')
                    elif user_operation == 4:
                        print(f'{"-" * 30}\n{getcurrency_current()}')
                    elif user_operation == 5:
                        print('5 - История курса валют.')
                        currency = input('Введите дату (формат дд.мм.гггг): ')
                        custom_date = input('Введите валюту для просмотра (USD, EUR, RUR, CHF, GBP, PLZ, SEK, XAU, CAD): ')
                        print(f'{"-" * 30}\n{getcurrency_history(currency, custom_date)}')
                    elif user_operation == 6:
                        print('6 - Конвертер валют. Конверсия может быть проведена только между UAH и другими валютами.')
                        curr_from = input('Введите стартовую валюту (Доступные валюты: UAH, USD, RUR, USD): ')
                        curr_to = input('Введите валюту для конвертирования (Доступные валюты: UAH, USD, RUR, USD): ')
                        curr_value = input('Введите сумму для конвертирования: ')
                        print(f'{"-" * 30}\n{curr_converter(curr_from, curr_to, curr_value)}')
                    elif user_operation == 7:
                        print('7 - Выход')
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
