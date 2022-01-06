# 7. Створити пустий клас, який називається Thing. Потім створіть об'єкт example цього класу. Виведіть типи зазначених об'єктів.

class Thing(object):

    def detect_type(self, example):
        return type(example)



example = Thing()

print(example.detect_type(1))
print(example.detect_type('asd'))
print(example.detect_type([1, 2, 3]))
