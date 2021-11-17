#3. Write a script to sum of the first n positive integers.

InputList = input("Enter the integers for summing (split with space): ")
InputList.split(" ")
SumList = []

for i in range(len(InputList)):
    if InputList[i].isdigit():
       SumList.append(InputList[i])
    
print(sum(map(int, SumList)))
