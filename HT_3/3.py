# 3. Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12),
# яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)

def season(month_num):
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
              9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    try:
        month_num = int(month_num)
        if 0 < month_num < 13:
            return f"Entered month = {months[month_num]}"
        else:
            return "Enter correct month number!"
    except:
        return "Enter correct month number!"


while True:
    month_number = season(input("Enter month number: "))
    if month_number != "Enter correct month number!":
        print(month_number)
        break
    else:
        print(month_number)
