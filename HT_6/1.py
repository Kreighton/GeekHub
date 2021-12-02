"""1. Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів.
   Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
   Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.
   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Green
      Yellow     Green
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green

"""

import time


def traffic_lights(end_point):
    auto_lights = 'Red'
    people_ligts = 'Green'
    sec_counter = 0
    try:
        for _ in range(end_point):
            time.sleep(1)
            if sec_counter == 4 and auto_lights != 'Yellow':
                auto_lights = 'Yellow'
            if sec_counter == 6:
                if people_ligts == 'Green':
                    auto_lights, people_ligts = 'Green', 'Red'
                else:
                    auto_lights, people_ligts = 'Red', 'Green'
                sec_counter = 0

            sec_counter += 1
            yield f'{auto_lights + " " * (11 - len(auto_lights))}{people_ligts}'
        yield 'Done.'
    except TypeError:
        yield "Error! Enter number!"


user_input = input('Enter number of traffic lights iterations: ')

for lights_iter in traffic_lights(user_input):
    print(lights_iter)
