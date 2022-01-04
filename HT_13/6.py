# 6. Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.

class CountSomeAtts(object):
    _counter = 0

    def __init__(self):
        CountSomeAtts._counter += 1
        self.id = CountSomeAtts._counter

    def __str__(self):
        return f'{self._counter}'


a = CountSomeAtts()
b = CountSomeAtts()
c = CountSomeAtts()

print(CountSomeAtts())
print(CountSomeAtts())
print(CountSomeAtts())
print(CountSomeAtts())
