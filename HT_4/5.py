# 5. Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.

def fibonacci_number(someNum):
    fibonacci_res = []
    try:
        someNum = int(someNum)
        if someNum > 0:
            for i in range(someNum):
                if i in (0, 1):
                    fibonacci_res.append(i)
                else:
                    fibonacci_res.append(fibonacci_res[i - 1] + fibonacci_res[i - 2])
            return fibonacci_res
        else:
            return "Error! Enter correct value!"
    except ValueError:
        return "Error! Enter correct value!"


test_digit = input("Enter digit for test: ")
print(fibonacci_number(test_digit))
