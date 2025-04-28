class BooleanAlgebra:
    def __init__(self, valueOne, valueTwo):
        self.valueOne = valueOne
        self.valueTwo = valueTwo

    def logicGatesTxt(self):
        print('''
            1> NOT Gate: Inverts A Value
            2> AND Gate: Returns True If Both Values Are True
            3> OR Gate: Returns True If Either of The Values Are True
            4> NAND Gate: Returns True If Not Both Values Are True
            5> NOR Gate: Returns True Only If Both Values Are False
            6> XOR Gate: Returns True If Exactly One Value Is True
            7> XNOR Gate: Returns True If Both Values Are Same
        ''')

    def logicGates(self, logicGate: int):
        if logicGate == 1:
            print(f'NOT {self.valueOne}: {not self.valueOne}')
        elif logicGate == 2:
            print(f"{self.valueOne} AND {self.valueTwo}: {self.valueOne and self.valueTwo}")
        elif logicGate == 3:
            print(f"{self.valueOne} OR {self.valueTwo}: {self.valueOne or self.valueTwo}")
        elif logicGate == 4:
            print(f"{self.valueOne} NAND {self.valueTwo}: {not (self.valueOne and self.valueTwo)}")
        elif logicGate == 5:
            print(f"{self.valueOne} NOR {self.valueTwo}: {not (self.valueOne or self.valueTwo)}")
        elif logicGate == 6:
            print(f"{self.valueOne} XOR {self.valueTwo}: {self.valueOne != self.valueTwo}")
        elif logicGate == 7:
            print(f"{self.valueOne} XNOR {self.valueTwo}: {self.valueOne == self.valueTwo}")
        else:
            print("Invalid Logic Gate!")
