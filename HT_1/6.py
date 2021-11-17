# 6. Write a script to check whether a specified value is contained in a group of values.
#       Test Data :
#        3 -> [1, 5, 8, 3] : True
#        -1 -> (1, 5, 8, 3) : False


# container = tuple(input("Container values: ").split(" "))
container = list(input("Container values: ").split(" "))
SearchedValue = input("Enter searched value: ")

print(f"{SearchedValue} -> {container}: {SearchedValue in container}")
