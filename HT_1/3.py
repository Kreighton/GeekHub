# 3. Write a script to sum of the first n positive integers.

NumOfSums = input("Enter number for summing: ")
SumOfNums = 0

for i in range(int(NumOfSums)):
    SumOfNums += (i+1)

print(SumOfNums)
