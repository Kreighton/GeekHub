'''
3. Напишіть програму, де клас «геометричні фігури» (figure) містить властивість color з початковим значенням white і метод для зміни кольору фігури,
а його підкласи «овал» (oval) і «квадрат» (square) містять методи __init__ для завдання початкових розмірів об'єктів при їх створенні.'''


class Figure(object):
    color = 'white'

    def change_color(self, color):
        self.color = color


class Oval(Figure):

    def __init__(self, far_distance, close_distance):
        self.far_distance = far_distance
        self.close_distance = close_distance


class Square(Figure):

    def __init__(self, side):
        self.side = side


sq_1 = Square(4)
print(sq_1.color, sq_1.side)
sq_1.change_color('black')
print(sq_1.color, sq_1.side)
