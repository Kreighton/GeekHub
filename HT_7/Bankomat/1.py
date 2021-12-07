"""1. Програма-банкомат.
   Створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.data>);
      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>) та історію транзакцій (файл <{username}_transactions.data>);
      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено число; знімається не більше, ніж є на рахунку).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
      - файл з користувачами: тільки читається. Якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
      - спочатку - логін користувача - програма запитує ім'я/пароль. Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )
      - потім - елементарне меню типа:
        Введіть дію:
           1. Продивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив :)

"""

import csv


class WrongLogin(Exception):
    pass


class WrongOperation(Exception):
    pass


def login_check(login, password, user_list):
    if [login, password] in user_list:
        return True
    else:
        return False


def check_balance(login):
    user_balance = open(f'{login}_balance.data', 'r').read()
    return user_balance


def add_balance(login):
    print('2 - Пополнение баланса')
    try:
        additional_funds = input("Введите сумму пополнения: ")
        if additional_funds.isdigit():
            user_balance = open(f'{login}_balance.data', 'r').read()
            user_funds = open(f'{login}_balance.data', 'w')
            user_funds.write(str(float(user_balance) + float(additional_funds)))
            user_funds.close()
            transactions = open(f'{login}_transactions.data', 'a')
            transactions.write(f'\n+{str(additional_funds)}')
            transactions.close()
            return additional_funds
        else:
            raise ValueError
    except ValueError:
        return


def drop_balance(login):
    print('3 - Снятие баланса')
    try:
        drop_funds = input("Введите сумму для снятия: ")
        if drop_funds.isdigit():
            user_balance = float(open(f'{login}_balance.data', 'r').read())
            drop_funds = float(drop_funds)
            if drop_funds > user_balance:
                return "Ошибка! Недостаточно средств на счету!"
            user_funds = open(f'{login}_balance.data', 'w')
            user_funds.write(str(user_balance - drop_funds))
            user_funds.close()
            transactions = open(f'{login}_transactions.data', 'a')
            transactions.write(f'\n-{str(drop_funds)}')
            transactions.close()
            return f'Успех! Вы сняли {drop_funds} у.е.'
        else:
            raise ValueError
    except ValueError:
        return


def start(login):
    try:
        while True:
            some_operation = int(input(f'{"-" * 40}\nДобро пожаловать, {login}! Выберите операцию:'
                                       '\n1.Просмотреть баланс.\n2.Пополнить баланс\n3.Снять деньги с баланса\n4.Выход\n'))
            if some_operation not in range(1, 5):
                raise WrongOperation()
            elif some_operation == 1:
                print(f'{"-" * 40}\nТекущий баланс пользователя {login} - {check_balance(login)}')
            elif some_operation == 2:
                print(f'{"-" * 40}\nУспех! Счёт пользователя {login} был пополнен на {add_balance(login)} у.е.')
            elif some_operation == 3:
                print(f'{"-" * 40}\n{drop_balance(login)}')
            elif some_operation == 4:
                return '4 - Закрытие программы'
    except ValueError:
        return 'Error! Enter correct values!'
    except WrongOperation:
        return 'Error! Wrong operation!'


login_counter = 0
users_csv = []

with open('users.data') as users:
    reader = csv.reader(users)
    for row in reader:
        users_csv.append(row)

while True:
    if login_counter == 3:
        print("Вы истратили 3 попытки ввода. Закрытие программы.")
        break
    try:
        user_login = input('Введите логин: ')
        user_password = input('Введите пароль: ')
        if login_check(user_login, user_password, users_csv):
            print(start(user_login))
            break
        else:
            raise WrongLogin()
    except WrongLogin:
        login_counter += 1
        print(f'Ошибка ввода логина или пароля! У вас осталось {3 - login_counter} попыток')
