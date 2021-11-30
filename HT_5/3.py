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


def check_login_pword(login_list):
    for i in login_list:
        try:
            print(f'Name: {i[0]}\nPassword: {i[1]}')
            if not (3 < len(i[0]) < 51):
                raise LoginNotFit(i[0])
            elif len(i[1]) < 8 or not (any(obj.isdigit() for obj in i[1])):
                raise PwordNotFit()
            elif i[0] == i[1]:
                raise StringsAreTheSame()
            else:
                print(f'Status: OK\n'+'-' * 5)
        except LoginNotFit as err:
            print(f'Status: Error, login is {err.lenlogin} symbols long\n'+'-' * 5)
        except PwordNotFit:
            print('Status: Error, password is too short or do not have numbers in it.\n'+'-' * 5)
        except StringsAreTheSame:
            print('Status: Login and Password are the same, password is too insecure!\n'+'-' * 5)


check_login_pword([['Pasha', '123'], ['Eugene', '1yuh2g3jgkh12'], ['Kyle', 'qwerty'], ['foo', 'bar'], ['Mat', 'rix']])
