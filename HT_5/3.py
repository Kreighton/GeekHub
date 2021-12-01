# 3. На основі попередньої функції створити наступний кусок кода:
#   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
#   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
#      Name: vasya
#      Password: wasd
#      Status: password must have at least one digit
#      -----
#      Name: vasya
#      Password: vasyapupkin2000
#      Status: OK
#   P.S. Не забудьте використати блок try/except ;)


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
        else:
            return 'OK'
    except LoginNotFit as err:
        return f'Status: Error, login is {err.lenlogin} symbols long'
    except PwordNotFit:
        return 'Error, password is too short or do not have numbers in it.'
    except StringsAreTheSame:
        return 'Login and Password are the same, password is too insecure!'


def login_pword_validate(login_list):
    total_result = ''
    for i in login_list:
        total_result += f'Name: {i[0]}\nPassword: {i[1]}\nStatus: {check_login_pword(i[0], i[1])}\n'+'-' * 5 + '\n'
    return total_result


print(login_pword_validate([['Pasha', '123'], ['Eugene', '1yuh2g3jgkh12'], ['Kyle', 'qwerty'], ['foo', 'bar'], ['Mat', 'rix']]))
