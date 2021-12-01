# 6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
#   P.S. Повинен вертатись генератор.
#   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range


class RangeError(Exception):
    pass


def custom_range(start=0, stop='', step=1):
    try:
        if step == 0 or type(start) != int:
            raise ValueError
        if stop == '' and start != 0:
            start, stop = 0, start
        if (stop - start > 0 and step < 0) or (stop - start < 0 and step > 0):
            raise RangeError
        iter_custom = start
        if step > 0:
            while iter_custom < stop:
                yield iter_custom
                iter_custom += step
        elif step < 0:
            while iter_custom > stop:
                yield iter_custom
                iter_custom += step
    except ValueError:
        yield ValueError
    except RangeError as err:
        yield err


a = [i for i in custom_range(20)]

print(a)
