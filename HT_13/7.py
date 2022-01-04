# 7. Створити пустий клас, який називається Thing. Потім створіть об'єкт example цього класу. Виведіть типи зазначених об'єктів.

class Thing(object):

    def __init__(self, object_type):
        self.object_type = type(object_type)

    def __str__(self):
        return f'{self.object_type}'


example = Thing('a')
print(example)

example = Thing(1)
print(example)

example = Thing(True)
print(example)

example = Thing([1, 2])
print(example)

example = Thing((1, 2))
print(example)

example = Thing({1: 2, 3: 4})
print(example)
