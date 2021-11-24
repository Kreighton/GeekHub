# 1. Створити цикл від 0 до ... (вводиться користувачем). В циклі створити умову, яка буде виводити поточне значення,
# якщо остача від ділення на 17 дорівнює 0.

number_input = int(input("Type number for test: "))

for i in range(number_input):
    if i % 17 == 0:
        print(f"{i} can be divided by 17 with 0 after \",\"")
        
