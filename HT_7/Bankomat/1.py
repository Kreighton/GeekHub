# Enter task here

import os
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


def start(login, password):
	try:
		while True:
			some_operation = int(input(f'{"-"*40}\nДобро пожаловать, {login}! Выберите операцию:'
				'\n1.Просмотреть баланс.\n2.Пополнить баланс\n3.Выход\n'))
			if some_operation not in range(1, 4):
				raise WrongOperation()
			elif some_operation == 1:
				print(f'{"-"*40}\nТекущий баланс пользователя {login} - {check_balance(login)}')
			elif some_operation == 2:
				print(f'{"-"*40}\nУспех! Счёт пользователя {login} был пополнен на {add_balance(login)} у.е.')
			elif some_operation == 3:
				return '3 - Закрытие программы'
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
		if login_check(user_login, user_password, users_csv) == True:
			print(start(user_login, user_password))
			break
		else:
			raise WrongLogin()
	except WrongLogin:
		login_counter += 1
		print(f'Ошибка ввода логина или пароля! У вас осталось {3-login_counter} попыток')



