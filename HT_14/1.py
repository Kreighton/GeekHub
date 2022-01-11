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


class Person(object):
    def __init__(self, login, password, incasator=False):
        self.login = login
        self.password = password
        self.incasator = incasator


class User(Person):
    def __init__(self, login, password, incasator=False):
        super(User, self).__init__(login, password, incasator)
        self.db_opers = DataBaseOperations(self.login)
        self.pb_opers = ParsePrivatBankOperations()
        self.balance = self.db_opers.check_balance()

    def show_money(self):
        print('1 - Просмотреть баланс')
        return f'Текущий баланс пользователя {self.login} = {self.balance} UAH'

    def add_money(self):
        print('2 - Пополнение баланса')
        try:
            additional_funds = float(input('Введите количество средств для пополнения: '))
            if additional_funds < 0:
                raise NegativeFunds()
            else:
                self.db_opers.add_balance(additional_funds)
                self.db_opers.add_transaction('add', additional_funds)
                return f'Поздравляем! Счёт пользователя {self.login} был пополнен на {additional_funds} у.е'

        except NegativeFunds:
            return 'Вы ввели некорректную сумму! Возврат в главное меню'
        except ValueError:
            return 'Вы ввели буквы! Возврат в главное меню'

    def give_money(self):
        print('3 - Снятие баланса')
        try:
            total_banknotes = self.db_opers.check_bankomat_funds()
            total_banknotes_dict = {total_banknotes[i][0]: total_banknotes[i][1] for i in range(len(total_banknotes))}
            print(f'{"-" * 40}\nДоступное количество купюр:')
            print('\n'.join(f'{key} = {total_banknotes_dict[key]}' for key in total_banknotes_dict))
            dropped_funds = int(input('Введите количество средств для снятия: '))

            if dropped_funds < 0:
                raise NegativeFunds()
            if dropped_funds > self.balance:
                raise InsufficientFunds()
            dropped_banknotes = {}
            rest_of_funds = dropped_funds

            for nominal in sorted(total_banknotes_dict, reverse=True):
                if not total_banknotes_dict[nominal]:
                    continue
                nominals_to_give = rest_of_funds // nominal
                if not nominals_to_give:
                    continue
                nominals_to_give = min(nominals_to_give, total_banknotes_dict[nominal])
                while nominals_to_give:
                    rest_of_funds = rest_of_funds - nominal * nominals_to_give
                    if not rest_of_funds:
                        dropped_banknotes[nominal] = nominals_to_give
                        break
                    for nominal2 in sorted(total_banknotes_dict, reverse=True):
                        if nominal2 >= nominal or not total_banknotes_dict[nominal2]:
                            continue
                        if rest_of_funds % nominal2 == 0:
                            break
                    else:
                        rest_of_funds = rest_of_funds + nominal * nominals_to_give
                        nominals_to_give -= 1
                        continue
                    dropped_banknotes[nominal] = nominals_to_give
                    break
                if not rest_of_funds:
                    break

            total_banknotes = [(total_banknotes_dict[key], key) for key in total_banknotes_dict]
            self.db_opers.drop_balance(self.balance, dropped_funds, total_banknotes)
            self.db_opers.add_transaction('drop', dropped_funds)
            result = ''
            for key in dropped_banknotes.keys():
                if dropped_banknotes[key] > 0:
                    result += f'\n{dropped_banknotes[key]} банкнот по {key}'
            return f'Поздравляем! Со счёта пользователя {self.login} было снято {dropped_funds} у.е.{result}'

        except NegativeFunds:
            return 'Вы ввели некорректную сумму! Возврат в главное меню'
        except InsufficientFunds:
            return 'Недостаточно средств! Возврат в главное меню'
        except ValueError:
            return 'Ошибка ввода! Возврат в главное меню'
        except InsufficientBanknotes:
            return 'В банкомате недостаточно средств! Возврат в главное меню'

    def today_currency(self):
        print('4 - Проверка курса валют')
        a = self.pb_opers.getcurrency_current()
        for i in range(len(a)):
            a[i]["buy"] = "%.2f" % float(a[i]["buy"])
            a[i]["sale"] = "%.2f" % float(a[i]["sale"])
        result = ''.join([f'{a[i]["ccy"]} к {a[i]["base_ccy"]}:\nПродажа: {a[i]["buy"]}\nПокупка: '
                          f'{a[i]["sale"]}\n{"-" * 40}\n' for i in range(len(a))])
        return result

    def history_currency(self):
        print('5 - История курса валют.')
        currencies = ["AZN", "BYN", "CAD", "CHF", "CNY", "CZK", "DKK", "EUR", "GBP", "HUF", "ILS", "JPY", "KZT", "MDL",
                      "NOK", "PLN", "RUB", "SEK", "SGD", "TMT", "TRY", "UAH", "USD", "UZS", "GEL"]
        custom_date = input('Введите дату (формат дд.мм.гггг): ')
        currency = input(f'Введите валюту для просмотра ({[", ".join(currencies)]}): ')
        try:
            if currency not in currencies:
                raise CurrencyNotExists()
            dd = int(custom_date[0:2])
            mm = int(custom_date[3:5])
            yyyy = int(custom_date[6:])
            if date(yyyy, mm, dd) > date.today():
                raise WrongDateInput()
            print(f'Currency: {currency}')
            for i in self.pb_opers.daterange(date(yyyy, mm, dd)):
                time.sleep(1)
                currency_hist_data = self.pb_opers.getcurrency(i.strftime("%d.%m.%Y"))
                print(f'Date: {i.strftime("%d.%m.%Y")}')
                if i == date.today():
                    print(''.join([f'NBU:    {currency_hist_data[cur]["saleRateNB"]}    -------\n'
                                   for cur in range(1, len(currency_hist_data)) if
                                   currency_hist_data[cur]["currency"] == currency]))

                else:
                    print(''.join([
                        f'NBU:    {currency_hist_data[cur]["saleRateNB"]}    {float(currency_hist_data[cur]["purchaseRateNB"] - currency_hist_data[cur]["saleRateNB"])}\n'
                        for cur in range(1, len(currency_hist_data)) if
                        currency_hist_data[cur].get('currency') == currency]))
            return 'Done!'
        except CurrencyNotExists:
            return 'Такой валюты не существует! Возврат в главное меню.'
        except WrongDateInput:
            return 'Неверно введенная дата! Возврат в главное меню'
        except ValueError:
            return 'Неверно введенная дата! Возврат в главное меню'
        except KeyError:
            return 'Error, Data is not updated!'

    def convert_currencies(self):
        print('6 - Конвертер валют.')
        curs_for_sale = ["AZN", "BYN", "CAD", "CHF", "CNY", "CZK", "DKK", "EUR", "GBP", "HUF", "ILS", "JPY",
                         "KZT", "MDL", "NOK", "PLN", "RUB", "SEK", "SGD", "TMT", "TRY", "UAH", "USD", "UZS", "GEL"]
        curr_from = input(f'Введите стартовую валюту (Доступные валюты: {", ".join(curs_for_sale)}): ')
        curr_to = input(f'Введите валюту для конвертирования (Доступные валюты: {", ".join(curs_for_sale)}): ')
        curr_value = input('Введите сумму для конвертирования: ')
        try:
            curr_value = float(curr_value)
            if curr_value < 0:
                raise ValueError()

            curs_for_sale = ["AZN", "BYN", "CAD", "CHF", "CNY", "CZK", "DKK", "EUR", "GBP", "HUF", "ILS", "JPY",
                             "KZT", "MDL", "NOK", "PLN", "RUB", "SEK", "SGD", "TMT", "TRY", "UAH", "USD", "UZS", "GEL"]
            if curr_from in curs_for_sale and curr_to in curs_for_sale:

                exchange_rate = self.pb_opers.get_changerate()
                converted_value = [exchange_rate[i].get('saleRateNB') for i in range(len(exchange_rate)) if
                                   exchange_rate[i].get('currency') == curr_from]
                if not converted_value:
                    exchange_rate = self.pb_opers.get_changerate(day='yesterday')

                if curr_from == curr_to:
                    result = curr_value
                elif curr_from == 'UAH':
                    move = [exchange_rate[i]['saleRateNB'] for i in range(1, len(exchange_rate)) if exchange_rate[i].get('currency') == curr_to][0]
                    result = curr_value / move
                elif curr_to == 'UAH':
                    move = [exchange_rate[i]['purchaseRateNB'] for i in range(1, len(exchange_rate)) if exchange_rate[i].get('currency') == curr_from][0]
                    result = curr_value * move
                else:
                    move_1 = [exchange_rate[i]['purchaseRateNB'] for i in range(1, len(exchange_rate)) if exchange_rate[i].get('currency') == curr_from][0]
                    move_2 = [exchange_rate[i]['saleRateNB'] for i in range(1, len(exchange_rate)) if exchange_rate[i].get('currency') == curr_to][0]
                    result = curr_value * move_1 / move_2
                return f"{curr_value} {curr_from} в {curr_to} = {result} {curr_to}"
            else:
                raise CurrencyNotExists
        except CurrencyNotExists:
            return 'Вы ввели неверную валюту! Возврат в главное меню.'
        except ValueError:
            return 'Введеная неверная валюта или сумма для обмена! Возврат в главное меню.'


class Incasator(Person):
    def __init__(self, login, password, incasator=False):
        super(Incasator, self).__init__(login, password, incasator)
        self.db_opers = DataBaseOperations(self.login)

    def check_banknotes(self):
        print('1 - Проверить количество купюр')
        result = ''
        total_banknotes = self.db_opers.check_bankomat_funds()
        for banknote in total_banknotes:
            result += f'Количество банкнот {banknote[0]} = {banknote[1]}\n'
        return result

    def add_banknotes(self):
        print('2 - Изменить кол-во купюр в банкомате')
        total_notes = [i[0] for i in self.db_opers.check_bankomat_funds()]
        try:
            banknotes_value = int(input('Введите купюру: '))
            banknotes_num = int(input('Введите количество купюр: '))
            if banknotes_num < 0:
                raise NegativeFunds()
            if banknotes_value not in total_notes:
                raise NoSuchBanknote()
            else:
                self.db_opers.change_notes(banknotes_value, banknotes_num)
                return f'Вы изменили кол-во банкнот {banknotes_value} на {banknotes_num} штук'
        except NegativeFunds:
            return 'Вы ввели некорректную сумму! Возврат в главное меню'
        except ValueError:
            return 'Ошибка ввода! Возврат в главное меню'
        except NoSuchBanknote:
            return 'Такой банкноты не существует! Возврат в главное меню'


class DataBaseOperations(object):
    def __init__(self, login):
        self.login = login

    def check_bankomat_funds(self):
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        total_banknotes = cur.execute('select banknote_value, banknote_total from banknotes').fetchall()
        con.close()
        return total_banknotes

    def change_notes(self, nominal, amount):
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        cur.execute('SELECT banknote_total FROM banknotes WHERE banknote_value=?', (nominal,)).fetchone()
        cur.execute('UPDATE banknotes SET banknote_total=? WHERE banknote_value=?', (amount, nominal))
        con.commit()
        con.close()
        return

    def add_transaction(self, operation, funds):
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        cur.execute(f'insert into {self.login}_transactions(operation, funds) values(?, ?)', (operation, funds))
        con.commit()
        con.close()
        return

    def check_balance(self):
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        user_id = cur.execute('select id from user_logs where user_login=?', (self.login,)).fetchone()
        user_balance = cur.execute('select user_balance from balance where id=?', (user_id[0],)).fetchone()
        con.close()
        return user_balance[0]

    def add_balance(self, funds):
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        user_id = cur.execute('select id from user_logs where user_login=?', (self.login,)).fetchone()
        user_funds = cur.execute('select user_balance from balance where id=?', (user_id[0],)).fetchone()
        cur.execute('UPDATE balance SET user_balance=? WHERE id=?',
                    (user_funds[0] + funds, user_id[0]))
        con.commit()
        con.close()
        return

    def drop_balance(self, balance, dropped_funds, total_banknotes):
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        cur.executemany('UPDATE banknotes SET banknote_total=? WHERE banknote_value=?', total_banknotes)
        user_id = cur.execute('select id from user_logs where user_login=?', (self.login,)).fetchone()
        cur.execute('UPDATE balance SET user_balance=? WHERE id=?', (balance - dropped_funds, user_id[0]))
        con.commit()
        con.close()
        return


class ParsePrivatBankOperations(object):

    def getcurrency_current(self):
        url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
        return requests.get(url=url).json()

    def daterange(self, custom_date):
        for i in range(int((date.today() - custom_date).days) + 1):
            yield custom_date + timedelta(i)

    def getcurrency(self, custom_date):
        url = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={custom_date}'
        return requests.get(url=url).json()['exchangeRate']

    def get_changerate(self, day='today'):
        if day == 'today':
            current_date = date.today().strftime("%d.%m.%Y")
        else:
            current_date = (date.today() - timedelta(days=1)).strftime("%d.%m.%Y")
        url = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={current_date}'
        result = requests.get(url=url).json()['exchangeRate']
        return result


class AuthCustom(object):

    def login_pword_check(self, login, pword):
        login_accepted = False
        incasation = False
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        is_account_exists = cur.execute('select is_incasator from user_logs where user_login=? and user_password=?',
                                        (login, pword)).fetchone()
        con.close()
        if is_account_exists:
            login_accepted = True
            if is_account_exists[0] == 1:
                incasation = True
        return login_accepted, incasation

    def start(self, login, pword, incasator=False):
        try:
            print("-" * 30)
            while True:
                if not incasator:
                    current_user = User(login, pword, incasator)
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
                            print(f'{"-" * 30}\n{current_user.show_money()}')
                        elif user_operation == 2:
                            print(f'{"-" * 30}\n{current_user.add_money()}')
                        elif user_operation == 3:
                            print(f'{"-" * 30}\n{current_user.give_money()}')
                        elif user_operation == 4:
                            print(f'{"-" * 30}\n{current_user.today_currency()}')
                        elif user_operation == 5:
                            print(f'{"-" * 30}\n{current_user.history_currency()}')
                        elif user_operation == 6:
                            print(f'{"-" * 30}\n{current_user.convert_currencies()}')
                        elif user_operation == 7:
                            print('7 - Выход')
                            return
                    else:
                        raise WrongOperationError()
                else:
                    current_user = Incasator(login, pword, incasator)
                    print(f'{"-" * 40}\nПриветствую, {login} (инкасатор) Выберите операцию!')
                    incas_operation = int(input('1. Проверить наличие купюр\n'
                                                '2. Изменить кол-во купюр в банкомате\n'
                                                '3. Выход\n'))
                    if incas_operation in range(1, 4):
                        if incas_operation == 1:
                            print(f'{"-" * 40}\n{current_user.check_banknotes()}')
                        if incas_operation == 2:
                            print(f'{"-" * 40}\n{current_user.add_banknotes()}')
                        if incas_operation == 3:
                            print('3 - Выход')
                            return
                    else:
                        raise WrongOperationError()

        except ValueError:
            return 'error'
        except WrongOperationError:
            return 'Введите правильный номер операции!'

def launch_bankomat():

    try_counter = 3

    while True:
        login_attempt = AuthCustom()
        if try_counter == 0:
            print(f'{"-" * 30}\nВы исчерпали 3 попытки! Закрытие программы.')
            break
        custom_login = input(f'{"-" * 30}\nВведите логин: ')
        custom_password = input('Введите пароль: ')
        access, incasator = login_attempt.login_pword_check(custom_login, custom_password)
        if access:
            login_attempt.start(custom_login, custom_password, incasator)
            break
        else:
            try_counter -= 1
            print(f'{"-" * 30}\nОшибка ввода логина/пароля. Осталось {try_counter} попыток')


launch_bankomat()
