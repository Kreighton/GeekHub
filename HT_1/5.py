# 5. Write a script to convert decimal to hexadecimal
#        Sample decimal number: 30, 4
#        Expected output: 1e, 04

print("Enter your decimal digits, separated by comma:")
digits = list(map(int, input().split(",")))
HexDigits = []

for i in range(len(digits)):
    HexDigits.append(format(digits[i], "02x"))

print(', '.join(HexDigits))
