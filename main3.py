#activity acp
decimal_number = int(input("Enter a decimal number: "))

if decimal_number == 0:
    print("The binary representation is: 0")
    
else:
    binary_number = "" 
    while decimal_number > 0:
        remainder = decimal_number % 2 
        temp_binary = ""
        for digit in binary_number:
            temp_binary += digit
        binary_number = str(remainder) + temp_binary

        decimal_number //= 2 
print(f"The binary representation is: {binary_number}")
