'''Сайт для виконання завдання: https://jsonplaceholder.typicode.com
Написати програму, яка буде робити наступне:
1. Робить запрос на https://jsonplaceholder.typicode.com/users і вертає коротку інформацію про користувачів (ID, ім'я, нікнейм)
2. Запропонувати обрати користувача (ввести ID)
3. Розробити наступну менюшку (із вкладеними пунктами):
   1. Повна інформація про користувача
   2. Пости:
      - перелік постів користувача (ID та заголовок)
      - інформація про конкретний пост (ID, заголовок, текст, кількість коментарів + перелік їхніх ID)
   3. ТУДУшка:
      - список невиконаних задач
      - список виконаних задач
   4. Вивести URL рандомної картинки
'''

import random
import requests
import json


def users_info_short():
    result = ''
    val_list = ['id', 'name', 'username']
    url = 'https://jsonplaceholder.typicode.com/users'
    temp = requests.get(url=url).json()
    for items in temp:
        result += ('\n').join([f'{val}: {items[val]}' for val in items if val in val_list]) + f'\n{"-" * 40}\n'
    return result


def user_info_id(us_id):
    try:
        us_id = int(us_id)
        if us_id <= 0:
            raise ValueError()
        else:
            url = f'https://jsonplaceholder.typicode.com/users?id={us_id}'
            temp = requests.get(url=url).json()
            if not temp:
                raise ValueError()
            else:
                temp = temp[0]
            for items in temp:
                if items == 'address' or items == 'company':
                    print(f'{items}:')
                    for val in temp[items]:
                        if val == 'geo':
                            print(f'    {val}:')
                            print(('\n').join([f'       {i}: {temp[items][val][i]}' for i in temp[items][val]]))
                        else:
                            print(f'    {val}: {temp[items][val]}')

                else:
                    print(f'{items}: {temp[items]}')
            return 'Done!'
    except ValueError:
        return 'Error, enter correct user ID!'


def all_post_ids_headers():
    result = ''
    val_list = ['id', 'title']
    url = 'https://jsonplaceholder.typicode.com/posts'
    temp = requests.get(url=url).json()
    for items in temp:
        result += ('\n').join([f'{val}: {items[val]}' for val in items if val in val_list]) + f'\n{"-" * 40}\n'
    return result


def get_post_byid(us_id):
    try:
        us_id = int(us_id)
        url_post = f'https://jsonplaceholder.typicode.com/posts?id={us_id}'
        url_comments = f'https://jsonplaceholder.typicode.com/comments?postId={us_id}'
        temp_post = requests.get(url=url_post).json()
        if not temp_post:
            raise ValueError()
        else:
            temp_post = temp_post[0]
        temp_comments = requests.get(url=url_comments).json()
        num_of_comments = len(temp_comments)
        print('\n'.join([f'{items}: {temp_post[items]}' for items in temp_post]))
        print(f'{"-" * 40}\nNumber of comments = {num_of_comments}')
        comments_ids = ', '.join(map(str, [temp_comments[id_c]['id'] for id_c in range(num_of_comments)]))
        return f'Commentary ID\'s = {comments_ids}'
    except ValueError:
        return 'Wrong input! Type correct post ID'


def todo_list(completed_status):
    try:
        if completed_status == 'Done':
            completed_status = 'true'
        elif completed_status == 'Undone':
            completed_status = 'false'
        else:
            raise ValueError()
        url = f'https://jsonplaceholder.typicode.com/todos?completed={completed_status}'
        temp = requests.get(url=url).json()
        for items in temp:
            print('\n'.join([f'{val}: {items[val]}' for val in items]))
            print('-' * 40)
        return 'Done!'
    except ValueError:
        return 'Wrong complete status input!'


def randomimage(rand_integer):
    url = f'https://jsonplaceholder.typicode.com/photos?id={rand_integer}'
    temp = requests.get(url=url).json()
    return f'Your random image url = {temp[0]["url"]}'


def startmenu():
    print('Hello! Choose menu item:')
    try:
        while True:
            user_input = int(input('1. Short info about all users\n'
                                   '2. All info by user ID\n'
                                   '3. All post id-s and headers\n'
                                   '4. All post info by ID\n'
                                   '5. View todo list\n'
                                   '6. Random image\n'
                                   '7. Exit\n'))
            if user_input not in range(1, 8):
                raise ValueError()
            else:
                if user_input == 1:
                    print(f'{users_info_short()}\n' + ('-' * 40))
                if user_input == 2:
                    c_id = input('Enter user ID: ')
                    print(f'{user_info_id(c_id)}\n' + ('-' * 40))
                if user_input == 3:
                    print(f'{all_post_ids_headers()}\n' + ('-' * 40))
                if user_input == 4:
                    p_id = input('Enter post ID: ')
                    print(f'{get_post_byid(p_id)}\n' + ('-' * 40))
                if user_input == 5:
                    todo_id_input = input('Enter completing status for todolist (Done or Undone): ')
                    print(f'{todo_list(todo_id_input)}\n' + ('-' * 40))
                if user_input == 6:
                    print(f'Random image:\n{randomimage(random.randint(1, 5001))}\n' + ('-' * 40))
                if user_input == 7:
                    return 'Exit' + ('-' * 40)
    except ValueError:
        return 'Enter correct menu item!'


startmenu()
