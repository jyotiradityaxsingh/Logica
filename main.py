from Logica import BooleanAlgebra, BinaryOperations, TruthTables, NumberSystemConversion

print(r'''
 /$$                           /$$                    
| $$                          |__/                    
| $$        /$$$$$$   /$$$$$$  /$$  /$$$$$$$  /$$$$$$ 
| $$       /$$__  $$ /$$__  $$| $$ /$$_____/ |____  $$
| $$      | $$  \ $$| $$  \ $$| $$| $$        /$$$$$$$
| $$      | $$  | $$| $$  | $$| $$| $$       /$$__  $$
| $$$$$$$$|  $$$$$$/|  $$$$$$$| $$|  $$$$$$$|  $$$$$$$
|________/ \______/  \____  $$|__/ \_______/ \_______/
                     /$$  \ $$                        
                    |  $$$$$$/                        
                     \______/                         
''')

print('''
Commands:

1> Boolean Algebra (Using Two Values)
2> Truth Tables
3> Binary Operations (Addition, Subtraction, Multiplication And Division)
4> Number System Conversion (Binary, Decimal, Hexadecimal)
''')

try:
    usrInput = int(input('> '))

    if usrInput == 1:
        print('''
            1> NOT Gate: Inverts A Value
            2> AND Gate: Returns True If Both Values Are True
            3> OR Gate: Returns True If Either of The Values Are True
            4> NAND Gate: Returns True If Not Both Values Are True
            5> NOR Gate: Returns True Only If Both Values Are False
            6> XOR Gate: Returns True If Exactly One Value Is True
            7> XNOR Gate: Returns True If Both Values Are Same
        ''')

        valueOneInput = input('Enter Value One (Either True or False)> ')
        valueTwoInput = input('Enter Value Two (Either True or False)> ')

        if valueOneInput not in ['True', 'False'] or valueTwoInput not in ['True', 'False']:
            print("Invalid Input! Please Enter 'True' or 'False' Only")
            exit()

        valueOne = valueOneInput == 'True'
        valueTwo = valueTwoInput == 'True'

        booleanAlgebraCls = BooleanAlgebra(valueOne, valueTwo)

        try:
            logicGate = int(input('Choose the logic gate (1-7): '))
            if logicGate not in range(1, 8):
                print("Invalid Logic Gate Selection! Please choose a number between 1 and 7.")
            else:
                booleanAlgebraCls.logicGates(logicGate)
        except ValueError:
            print("Invalid Input! Please Enter A Number Between 1 And 7")

    elif usrInput == 2:
        valueOneInput = input('Enter Value One (Either True or False)> ')
        valueTwoInput = input('Enter Value Two (Either True or False)> ')

        if valueOneInput not in ['True', 'False'] or valueTwoInput not in ['True', 'False']:
            print("Invalid Input! Please Enter 'True' or 'False' Only")
            exit()

        valueOne = valueOneInput == 'True'
        valueTwo = valueTwoInput == 'True'

        truthTablesCls = TruthTables(valueOne, valueTwo)
        print(truthTablesCls.generateTable())

    elif usrInput == 3:
        print('''
            1> Addition
            2> Subtraction
            3> Multiplication
            4> Division
        ''')

        try:
            operation = int(input('Enter Operation> '))
            if operation not in range(1, 5):
                print("Invalid Operation! Please Choose A Number Between 1 And 4")
                exit()

            try:
                varOne = int(input('Enter Value One> '))
                varTwo = int(input('Enter Value Two> '))
            except ValueError:
                print("Invalid Input! Please Enter Valid Integers For Binary Operations.")
                exit()

            binaryOperationsCls = BinaryOperations(varOne, varTwo)

            if operation == 1:
                binaryOperationsCls.binaryAddition()
            elif operation == 2:
                binaryOperationsCls.binarySubtraction()
            elif operation == 3:
                binaryOperationsCls.binaryMultiplication()
            elif operation == 4:
                binaryOperationsCls.binaryDivision()

        except ValueError:
            print("Invalid Operation Input! Please Enter A Number Between 1 And 4")

    elif usrInput == 4:
        print('''
        1> Convert Binary to Decimal
        2> Convert Binary to Hexadecimal
        3> Convert Decimal to Binary
        4> Convert Decimal to Hexadecimal
        5> Convert Hexadecimal to Binary
        6> Convert Hexadecimal to Decimal
        ''')

        operation = int(input('Enter Operation> '))
        
        if operation == 1:
            binaryValue = input('Enter Binary Value> ')
            decimalResult = NumberSystemConversion.binaryToDecimal(binaryValue)
            print(f"Binary {binaryValue} To Decimal: {decimalResult}")

        elif operation == 2:
            binaryValue = input('Enter Binary Value> ')
            hexadecimalResult = NumberSystemConversion.binaryToHexadecimal(binaryValue)
            print(f"Binary {binaryValue} To Hexadecimal: {hexadecimalResult}")

        elif operation == 3:
            decimal_value = int(input('Enter Decimal Value> '))
            binary_result = NumberSystemConversion.decimalToBinary(decimal_value)
            print(f"Decimal {decimal_value} To Binary: {binary_result}")

        elif operation == 4:
            decimal_value = int(input('Enter Decimal Value> '))
            hexadecimalResult = NumberSystemConversion.decimalToHexadecimal(decimal_value)
            print(f"Decimal {decimal_value} To Hexadecimal: {hexadecimalResult}")

        elif operation == 5:
            hexadecimal_value = input('Enter Hexadecimal Value> ')
            binary_result = NumberSystemConversion.hexadecimalToBinary(hexadecimal_value)
            print(f"Hexadecimal {hexadecimal_value} To Binary: {binary_result}")

        elif operation == 6:
            hexadecimal_value = input('Enter Hexadecimal Value> ')
            decimalResult = NumberSystemConversion.hexadecimalToDecimal(hexadecimal_value)
            print(f"Hexadecimal {hexadecimal_value} To Decimal: {decimalResult}")

        else:
            print("Invalid Input! Please Choose A Valid Operation (1-6)")

    else:
        print("Invalid Command Input! Please Enter A Valid Integer For Command Selection")

except ValueError:
    print("Invalid Command Input! Please Enter A Valid Integer For Command Selection")
