# 1 .Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
#        Sample data : 1, 5, 7, 23
#        Output :
#        List : [‘1', ' 5', ' 7', ' 23']
#        Tuple : (‘1', ' 5', ' 7', ' 23')

print("Enter the numbers (separate with comma):")
MainInput = input()

mList = list(MainInput.split(","))
mTulpe = tuple(MainInput.split(","))

print(f"List: {mList}")
print(f"Tuple: {mTulpe}")
