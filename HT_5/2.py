# 2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
#   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
#   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
#   - щось своє :)
#   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.

class LoginNotFit(Exception):
    def __init__(self, login):
        self.lenlogin = len(login)


class PwordNotFit(Exception):
    pass

class StringsAreTheSame(Exception):
    pass


def check_login_pword(login, pword):
    try:
        if not (3 < len(login) < 51):
            raise LoginNotFit(login)
        elif len(pword) < 8 or not (any(i.isdigit() for i in pword)):
            raise PwordNotFit()
        elif login == pword:
            raise StringsAreTheSame()
    except LoginNotFit as err:
        return f'Error, login is {err.lenlogin} symbols long'
    except PwordNotFit:
        return 'Error, password is too short or do not have numbers in it.'
    except StringsAreTheSame:
        return 'Login and Password are the same, password is too insecure!'


print(check_login_pword(input('Enter login: '), input('Enter password: ')))
