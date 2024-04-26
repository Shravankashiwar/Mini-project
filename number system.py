def decimal_to_binary(n):
    return bin(n).replace("0b", "")

def binary_to_decimal(n):
    return int(n, 2)

def decimal_to_octal(n):
    return oct(n).replace("0o", "")

def octal_to_decimal(n):
    return int(n, 8)

def decimal_to_hexadecimal(n):
    return hex(n).replace("0x", "").upper()

def hexadecimal_to_decimal(n):
    return int(n, 16)

def convert_number():
    print("Select conversion:")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    print("3. Decimal to Octal")
    print("4. Octal to Decimal")
    print("5. Decimal to Hexadecimal")
    print("6. Hexadecimal to Decimal")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice == '1':
        decimal_number = int(input("Enter decimal number: "))
        print("Binary:", decimal_to_binary(decimal_number))
    elif choice == '2':
        binary_number = input("Enter binary number: ")
        print("Decimal:", binary_to_decimal(binary_number))
    elif choice == '3':
        decimal_number = int(input("Enter decimal number: "))
        print("Octal:", decimal_to_octal(decimal_number))
    elif choice == '4':
        octal_number = input("Enter octal number: ")
        print("Decimal:", octal_to_decimal(octal_number))
    elif choice == '5':
        decimal_number = int(input("Enter decimal number: "))
        print("Hexadecimal:", decimal_to_hexadecimal(decimal_number))
    elif choice == '6':
        hexadecimal_number = input("Enter hexadecimal number: ")
        print("Decimal:", hexadecimal_to_decimal(hexadecimal_number))
    else:
        print("Invalid Input")

convert_number()