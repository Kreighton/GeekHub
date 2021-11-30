# 1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
#   Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
#   Логіка наступна:
#       якщо введено коректну пару ім'я/пароль - вертається <True>;
#       якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>, інакше (<silent> == <False>) - породжується виключення LoginException


class LoginException(Exception):
    def __init__(self, silent):
        self.silent = silent



def login_check(login, pword, silent=False):
    login_logs = [['Pasha', '123'], ['', ''], ['', ''], ['', ''], ['', '']]
    try:
        if [login, pword] in login_logs:
            return True
        elif silent:
            return False
        else:
            raise LoginException(silent)

    except LoginException as err:
        return f'User not found. Silent = {err.silent}. Exception raised'


def login_enter():
    return input("Enter login: ")


def pword_enter():
    return input("Enter password: ")


def silent():
    loc_silent = input("Enter silent, leave blank for default (False): ")
    if loc_silent == 'True':
        return True
    else:
        return False


print(login_check(login_enter(), pword_enter(), silent()))
