# 6. Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
#   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
# -  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
# -  якщо довжина бульше 50 - > ваша фантазiя


def count_your_string(test_case):
    test_list = [i for i in test_case]
    test_digits = []
    test_not_digits = []
    more_than_fifty = ""
    count = 0
    for i in test_case:
        if i.isdigit():
            test_digits.append(int(i))
        elif i.isalpha():
            test_not_digits.append(i)

    if len(test_list) > 50:
        return "wat"
    elif len(test_list) < 30:
        return f"Sum = {sum(test_digits)}\nAll letters = {test_not_digits}"
    else:
        test_list.sort()
        for i in range(len(test_list)):
            try:
                if test_list[i] == test_list[i + 1]:
                    count += 1
                else:
                    more_than_fifty += f'Number of \'{test_list[i]}\' symbol in list = {count}\n'
                    count = 0
            except IndexError:
                return more_than_fifty


test_input = input("Enter random string: ")

print(count_your_string(test_input))
