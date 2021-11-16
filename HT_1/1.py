#Task 1
print("Enter the numbers (separate with comma):")
MainInput = input()

mList = list(MainInput.split(","))
mTulpe = tuple(MainInput.split(","))

print(f"List: {mList}")
print(f"Tuple: {mTulpe}")
