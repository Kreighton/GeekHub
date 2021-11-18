NumOfSums = 0
SumOfNums = 0

while True:
    try:
        NumOfSums = int(input("Enter number for summing: "))
        break
    except ValueError:
        print("This was not the number!")


for i in range(NumOfSums):
    SumOfNums += i+1

print(SumOfNums)
