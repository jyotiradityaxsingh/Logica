from Logica import BooleanAlgebra  # Assuming the 'BooleanAlgebra' class is defined in 'Logica.py'

print('''
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
''')

usrInput = input('> ')

try:
    usrInput = int(usrInput)
    
    if usrInput == 1:
        valueOneInput = input('Enter Value One (Either True or False)> ')
        valueTwoInput = input('Enter Value Two (Either True or False)> ')
        
        # Converts To Boolean
        try:
            valueOne = eval(valueOneInput.title())  # Converts 'True'/'False' String To Actual Boolean
            valueTwo = eval(valueTwoInput.title())  # Converts 'True'/'False' String To Actual Boolean
        except (NameError, SyntaxError):
            print("Invalid Input! Please Enter 'True' or 'False' Only")
            exit()

        BooleanAlgebraCls = BooleanAlgebra(valueOne, valueTwo)
        
        BooleanAlgebraCls.logicGatesTxt()
        
        # Get User Choice For Logic Gate
        try:
            logicGate = int(input('Choose the logic gate (1-7): '))
            BooleanAlgebraCls.logicGates(logicGate)
        except ValueError:
            print("Invalid Input! Please Enter A Number Between 1 And 7")
        
except ValueError:
    print("Invalid Command Input! Please Enter A Valid Integer For Command Selection")
