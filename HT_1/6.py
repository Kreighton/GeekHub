# 6. Write a script to check whether a specified value is contained in a group of values.
#       Test Data :
#        3 -> [1, 5, 8, 3] : True
#        -1 -> (1, 5, 8, 3) : False

TypeOfInput = ""

while True:
    try:
        TypeOfInput = int(input("List or Tuple? (1 - List, 2 - Tuple): "))
        if int(TypeOfInput) == 1 or int(TypeOfInput) == 2:
            break
        else:
            print("Enter correct value!")
    except ValueError:
        print("Enter correct value!")


if TypeOfInput == "1":
    container = list(input("You choose 1. Enter list values, separated with spaces: ").split(" "))
elif TypeOfInput == "2":
    container = tuple(input("You choose 2. Enter tuple values, separated with spaces: ").split(" "))

SearchedValue = input("Enter searched value: ")

print(f"{SearchedValue} -> {container}: {SearchedValue in container}")
