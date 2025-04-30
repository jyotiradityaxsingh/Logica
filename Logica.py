from tabulate import tab

class BooleanAlgebra:
    """
    A Class To Handle Boolean Algebra Operations Using Two Boolean Values.

    Attributes:
        valueOne (bool): The First Boolean Value.
        valueTwo (bool): The Second Boolean Value.
    """

    def __init__(self, valueOne: bool, valueTwo: bool):
        """
        Initializes The BooleanAlgebra Class With Two Boolean Values.

        Args:
            valueOne (bool): The First Boolean Value.
            valueTwo (bool): The Second Boolean Value.

        Raises:
            TypeError: If valueOne Or valueTwo Is Not A Boolean.
        """
        if not (isinstance(valueOne, bool) and isinstance(valueTwo, bool)):
            raise TypeError("Both valueOne and valueTwo must be booleans")
        self.valueOne = valueOne
        self.valueTwo = valueTwo

    def logicGates(self, logicGate: int) -> bool:
        """
        Performs A Logic Gate Operation Based On The Input Logic Gate Number.

        Args:
            logicGate (int): The Logic Gate To Perform (1-7).
                1: NOT (valueOne), 2: AND, 3: OR, 4: NAND, 5: NOR, 6: XOR, 7: XNOR.

        Returns:
            bool: The Result Of The Logic Gate Operation.

        Raises:
            ValueError: If logicGate Is Not In The Range 1-7.
        """
        if not isinstance(logicGate, int) or logicGate < 1 or logicGate > 7:
            raise ValueError("logicGate must be an integer between 1 and 7")

        if logicGate == 1:
            return not self.valueOne
        elif logicGate == 2:
            return self.valueOne and self.valueTwo
        elif logicGate == 3:
            return self.valueOne or self.valueTwo
        elif logicGate == 4:
            return not (self.valueOne and self.valueTwo)
        elif logicGate == 5:
            return not (self.valueOne or self.valueTwo)
        elif logicGate == 6:
            return self.valueOne != self.valueTwo
        elif logicGate == 7:
            return self.valueOne == self.valueTwo


class BinaryOperations:
    """
    A Class To Perform Basic Binary Operations: Addition, Subtraction, Multiplication, And Division.

    Attributes:
        valueOne (int): The First Integer Value.
        valueTwo (int): The Second Integer Value.
    """

    def __init__(self, valueOne: int, valueTwo: int):
        """
        Initializes The BinaryOperations Class With Two Integer Values.

        Args:
            valueOne (int): The First Integer Value.
            valueTwo (int): The Second Integer Value.

        Raises:
            TypeError: If valueOne Or valueTwo Is Not An Integer.
        """
        if not (isinstance(valueOne, int) and isinstance(valueTwo, int)):
            raise TypeError("Both valueOne and valueTwo must be integers")
        self.valueOne = valueOne
        self.valueTwo = valueTwo

    def binaryAddition(self) -> str:
        """
        Performs Binary Addition, Showing Intermediate Steps.

        Returns:
            str: The Binary Result Of The Addition.

        Raises:
            ValueError: If Inputs Are Negative.
        """
        if self.valueOne < 0 or self.valueTwo < 0:
            raise ValueError("Negative numbers are not supported")
        
        varOne = bin(self.valueOne)[2:]
        varTwo = bin(self.valueTwo)[2:]
        maxLength = max(len(varOne), len(varTwo))
        varOne = varOne.zfill(maxLength)
        varTwo = varTwo.zfill(maxLength)

        carry = 0
        result = []
        print("Performing Binary Addition:")
        for i in range(maxLength - 1, -1, -1):
            bitSum = int(varOne[i]) + int(varTwo[i]) + carry
            result.insert(0, str(bitSum % 2))
            carry = bitSum // 2
            print(f"Bit {i}: {varOne[i]} + {varTwo[i]} + {carry if i < maxLength - 1 else 0} = {bitSum} -> {result[0]}")

        if carry:
            result.insert(0, '1')
            print(f"Final Carry: 1")

        finalResult = ''.join(result)
        print(f"Final Sum (Binary): {finalResult}")
        return finalResult

    def binarySubtraction(self) -> str:
        """
        Performs Binary Subtraction Using Two's Complement, Showing Intermediate Steps.

        Returns:
            str: The Binary Result Of The Subtraction.

        Raises:
            ValueError: If Inputs Are Negative.
        """
        if self.valueOne < 0 or self.valueTwo < 0:
            raise ValueError("Negative numbers are not supported")

        varOne = bin(self.valueOne)[2:]
        varTwo = bin(self.valueTwo)[2:]
        maxLength = max(len(varOne), len(varTwo))
        varOne = varOne.zfill(maxLength)
        varTwo = varTwo.zfill(maxLength)

        # Two's complement of varTwo
        varTwoComplement = bin((1 << maxLength) - int(varTwo, 2))[2:].zfill(maxLength)
        print(f"Performing Binary Subtraction: {varOne} - {varTwo}")
        print(f"Two's Complement of {varTwo}: {varTwoComplement}")

        carry = 0
        result = []
        for i in range(maxLength - 1, -1, -1):
            bitSum = int(varOne[i]) + int(varTwoComplement[i]) + carry
            result.insert(0, str(bitSum % 2))
            carry = bitSum // 2
            print(f"Bit {i}: {varOne[i]} + {varTwoComplement[i]} + {carry if i < maxLength - 1 else 0} = {bitSum} -> {result[0]}")

        finalResult = ''.join(result)
        print(f"Result (Binary): {finalResult}")
        return finalResult

    def binaryMultiplication(self) -> str:
        """
        Performs Binary Multiplication Using Shift-And-Add, Showing Intermediate Steps.

        Returns:
            str: The Binary Result Of The Multiplication.

        Raises:
            ValueError: If Inputs Are Negative.
        """
        if self.valueOne < 0 or self.valueTwo < 0:
            raise ValueError("Negative numbers are not supported")

        varOne = bin(self.valueOne)[2:]
        varTwo = bin(self.valueTwo)[2:]
        print(f"Performing Binary Multiplication: {varOne} * {varTwo}")

        result = 0
        for i, bit in enumerate(reversed(varTwo)):
            if bit == '1':
                shifted = self.valueOne << i
                result += shifted
                print(f"Bit {i}: {varOne} << {i} = {bin(shifted)[2:]}")
        
        resultBin = bin(result)[2:]
        print(f"Result (Binary): {resultBin}")
        return resultBin

    def binaryDivision(self) -> tuple[str, str]:
        """
        Performs Binary Division, Showing Quotient And Remainder In Binary.

        Returns:
            tuple[str, str]: The Binary Quotient And Remainder.

        Raises:
            ValueError: If Dividing By Zero Or Inputs Are Negative.
        """
        if self.valueTwo == 0:
            raise ValueError("Division by zero is not allowed")
        if self.valueOne < 0 or self.valueTwo < 0:
            raise ValueError("Negative numbers are not supported")

        print(f"Performing Binary Division: {self.valueOne} // {self.valueTwo}")
        quotient = self.valueOne // self.valueTwo
        remainder = self.valueOne % self.valueTwo

        quotientBin = bin(quotient)[2:]
        remainderBin = bin(remainder)[2:]
        print(f"Quotient (Binary): {quotientBin}")
        print(f"Remainder (Binary): {remainderBin}")
        return quotientBin, remainderBin

class TruthTables:
    """
    A Class To Generate Truth Tables For Basic Logical Operations Using Two Boolean Values.
    """

    def __init__(self, valueOne: bool, valueTwo: bool):
        """
        Initializes The TruthTables Class With Two Boolean Values.

        Args:
            valueOne (bool): The First Boolean Value.
            valueTwo (bool): The Second Boolean Value.
        """
        if not (isinstance(valueOne, bool) and isinstance(valueTwo, bool)):
            raise TypeError("Both valueOne and valueTwo must be booleans")
        self.valueOne = valueOne
        self.valueTwo = valueTwo

    def generateTable(self) -> str:
        """
        Generates A Truth Table For Common Logical Operations (AND, OR, NOT, etc.).

        Returns:
            str: A Neatly Formatted Truth Table For Various Logical Operations.
        """
        headers = ["valueOne", "valueTwo", "NOT valueOne", "valueOne AND valueTwo", "valueOne OR valueTwo", 
                   "valueOne XOR valueTwo", "valueOne NAND valueTwo", "valueOne NOR valueTwo", "valueOne XNOR valueTwo"]
        
        table = []
        table.append([self.valueOne, self.valueTwo, 
                      not self.valueOne, 
                      self.valueOne and self.valueTwo, 
                      self.valueOne or self.valueTwo,
                      self.valueOne != self.valueTwo, 
                      not (self.valueOne and self.valueTwo), 
                      not (self.valueOne or self.valueTwo), 
                      self.valueOne == self.valueTwo])

        return tabulate(table, headers, tablefmt="grid")