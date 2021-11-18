# 6. Write a script to check whether a specified value is contained in a group of values.
#       Test Data :
#        3 -> [1, 5, 8, 3] : True
#        -1 -> (1, 5, 8, 3) : False

TypeOfInput = ""

while TypeOfInput != "1" or TypeOfInput != "2":
    TypeOfInput = input("List or Tuple? (1 - List, 2 - Tuple): ")
    if TypeOfInput.isdigit():
        if int(TypeOfInput) <= 0 or int(TypeOfInput) > 2:
            print("Enter correct value!")
        else:
            break
    else:
        print("Enter correct value!")


if TypeOfInput == "1":
    container = list(input("You choose 1. Enter list values: ").split(" "))
elif TypeOfInput == "2":
    container = tuple(input("You choose 2. Enter tuple values: ").split(" "))

SearchedValue = input("Enter searched value: ")

print(f"{SearchedValue} -> {container}: {SearchedValue in container}")
