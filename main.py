from Logica import BooleanAlgebra, BinaryOperations, TruthTables, NumberSystemConversion, KarnaughMap

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
3> Binary Operations (Addition, Subtraction, Multiplication, Division, Shifts and Rotates)
4> Number System Conversion (Binary, Decimal, Hexadecimal)
5> Karnaugh Map Simplification (2-variable or 3-variable)
''')

try:
    usrInput = int(input('> '))

    if usrInput == 1:
        print()

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
                print(f"Result: {booleanAlgebraCls.logicGates(logicGate)}")
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
        print()

        try:
            operation = int(input('Enter Operation> '))
            if operation not in range(1, 11):
                print("Invalid Operation! Please Choose A Number Between 1 And 10")
                exit()

            try:
                varOne = int(input('Enter Value One> '))

                varTwo = 0 if operation in range(5, 11) else int(input('Enter Value Two> '))
            except ValueError:
                print("Invalid Input! Please Enter Valid Integers For Binary Operations.")
                exit()

            binaryOperationsCls = BinaryOperations(varOne, varTwo)

            if operation == 1:
                print(f"Addition Result: {binaryOperationsCls.binaryAddition()}")
            elif operation == 2:
                print(f"Subtraction Result: {binaryOperationsCls.binarySubtraction()}")
            elif operation == 3:
                print(f"Multiplication Result: {binaryOperationsCls.binaryMultiplication()}")
            elif operation == 4:
                print(f"Division Result: {binaryOperationsCls.binaryDivision()}")
            elif operation == 5:
                positions = int(input("Enter Number of Positions To Shift Left: "))
                print(f"Logical Left Shift Result: {binaryOperationsCls.logicalLeftShift(positions)}")
            elif operation == 6:
                positions = int(input("Enter Number of Positions To Shift Right: "))
                print(f"Logical Right Shift Result: {binaryOperationsCls.logicalRightShift(positions)}")
            elif operation == 7:
                positions = int(input("Enter Number of Positions To Shift Left: "))
                print(f"Arithmetic Left Shift Result: {binaryOperationsCls.arithmeticLeftShift(positions)}")
            elif operation == 8:
                positions = int(input("Enter Number of Positions To Shift Right: "))
                print(f"Arithmetic Right Shift Result: {binaryOperationsCls.arithmeticRightShift(positions)}")
            elif operation == 9:
                positions = int(input("Enter Number of Positions To Rotate Left: "))
                print(f"Rotate Left Shift Result: {binaryOperationsCls.rotateLeftShift(positions)}")
            elif operation == 10:
                positions = int(input("Enter Number of Positions To Rotate Right: "))
                print(f"Rotate Right Shift Result: {binaryOperationsCls.rotateRightShift(positions)}")

        except ValueError:
            print("Invalid Operation Input! Please Enter A Number Between 1 And 10")

    elif usrInput == 4:
        print()

        try:
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

        except ValueError:
            print("Invalid Input! Please Enter A Valid Operation (1-6)")

    elif usrInput == 5:
        print()

        try:
            kmapValuesInput = input('Enter K-map Values (4 Values For 2-Variable or 8 Values For 3-Variable, Separated By Commas)> ')
            kmapValues = [int(x) for x in kmapValuesInput.split(',')]

            if len(kmapValues) not in [4, 8]:
                print("Invalid Input! Please Enter Either 4 Values For 2-Variable or 8 Values For 3-Variable K-Map")
                exit()

            kmapCls = KarnaughMap(kmapValues)
            print("K-Map Table:")
            print(kmapCls.generateKmap())
            print("Simplified Expression:")
            print(kmapCls.simplifyExpression())

        except ValueError:
            print("Invalid Input! Please Enter Valid Integers For K-Map Values")

    else:
        print("Invalid Command Input! Please Enter A Valid Integer For Command Selection")

except ValueError:
    print("Invalid Command Input! Please Enter A Valid Integer For Command Selection")
