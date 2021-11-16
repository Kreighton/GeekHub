# 4. Write a script to concatenate N strings.

NumOfStrs = input("How much strings you want to use: ")
concatenateStrs = ""

for i in range(int(NumOfStrs)):
    concatenateStrs += input(f"Enter your {i+1} string: ")

print(f"Result = \"{concatenateStrs}\"")
