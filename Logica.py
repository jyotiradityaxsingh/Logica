from tabulate import tabulate

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
    A Class To Perform Basic Binary Operations: Addition, Subtraction, Multiplication, Division, and Shifts.

    Attributes:
        valueOne (int): The First Integer Value.
        valueTwo (int): The Second Integer Value.
    """

    def __init__(self, valueOne: int, valueTwo: int):
        if not (isinstance(valueOne, int) and isinstance(valueTwo, int)):
            raise TypeError("Both valueOne and valueTwo must be integers")
        self.valueOne = valueOne
        self.valueTwo = valueTwo

    def binaryAddition(self) -> str:
        if self.valueOne < 0 or self.valueTwo < 0:
            raise ValueError("Negative numbers are not supported")

        varOne = bin(self.valueOne)[2:]
        varTwo = bin(self.valueTwo)[2:]
        maxLength = max(len(varOne), len(varTwo))
        varOne = varOne.zfill(maxLength)
        varTwo = varTwo.zfill(maxLength)

        carry = 0
        result = []
        for i in range(maxLength - 1, -1, -1):
            bitSum = int(varOne[i]) + int(varTwo[i]) + carry
            result.insert(0, str(bitSum % 2))
            carry = bitSum // 2

        if carry:
            result.insert(0, '1')

        return ''.join(result)

    def binarySubtraction(self) -> str:
        if self.valueOne < 0 or self.valueTwo < 0:
            raise ValueError("Negative numbers are not supported")

        varOne = bin(self.valueOne)[2:]
        varTwo = bin(self.valueTwo)[2:]
        maxLength = max(len(varOne), len(varTwo))
        varOne = varOne.zfill(maxLength)
        varTwo = varTwo.zfill(maxLength)

        varTwoComplement = bin((1 << maxLength) - int(varTwo, 2))[2:].zfill(maxLength)
        carry = 0
        result = []
        for i in range(maxLength - 1, -1, -1):
            bitSum = int(varOne[i]) + int(varTwoComplement[i]) + carry
            result.insert(0, str(bitSum % 2))
            carry = bitSum // 2

        return ''.join(result)

    def binaryMultiplication(self) -> str:
        if self.valueOne < 0 or self.valueTwo < 0:
            raise ValueError("Negative numbers are not supported")

        result = 0
        for i, bit in enumerate(reversed(bin(self.valueTwo)[2:])):
            if bit == '1':
                result += self.valueOne << i

        return bin(result)[2:]

    def binaryDivision(self) -> tuple[str, str]:
        if self.valueTwo == 0:
            raise ValueError("Division by zero is not allowed")
        if self.valueOne < 0 or self.valueTwo < 0:
            raise ValueError("Negative numbers are not supported")

        quotient = self.valueOne // self.valueTwo
        remainder = self.valueOne % self.valueTwo

        return bin(quotient)[2:], bin(remainder)[2:]

    def logicalLeftShift(self, positions: int) -> str:
        return bin(self.valueOne << positions)[2:]

    def logicalRightShift(self, positions: int) -> str:
        return bin(self.valueOne >> positions)[2:]

    def arithmeticLeftShift(self, positions: int) -> str:
        return bin(self.valueOne << positions)[2:]

    def arithmeticRightShift(self, positions: int) -> str:
        if self.valueOne < 0:
            result = (self.valueOne >> positions) | (1 << (positions - 1)) if positions else self.valueOne
        else:
            result = self.valueOne >> positions
        return bin(result)[2:]

    def rotateLeftShift(self, positions: int) -> str:
        bitLength = self.valueOne.bit_length()
        positions %= bitLength
        result = ((self.valueOne << positions) | (self.valueOne >> (bitLength - positions))) & ((1 << bitLength) - 1)
        return bin(result)[2:].zfill(bitLength)

    def rotateRightShift(self, positions: int) -> str:
        bitLength = self.valueOne.bit_length()
        positions %= bitLength
        result = ((self.valueOne >> positions) | (self.valueOne << (bitLength - positions))) & ((1 << bitLength) - 1)
        return bin(result)[2:].zfill(bitLength)

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

class NumberSystemConversion:
    """
    A Class To Handle Conversion Between Binary, Decimal, And Hexadecimal Formats.
    """

    @staticmethod
    def decimalToBinary(decimal: int) -> str:
        """
        Converts a Decimal Number To Binary Representation.
        
        Args:
            decimal (int): The Decimal Number To Convert.
        
        Returns:
            str: The Binary Representation.
        """
        if decimal < 0:
            raise ValueError("Negative numbers are not supported")
        return bin(decimal)[2:]

    @staticmethod
    def decimalToHexadecimal(decimal: int) -> str:
        """
        Converts a Decimal Number To Hexadecimal Representation.
        
        Args:
            decimal (int): The Decimal Number To Convert.
        
        Returns:
            str: The Hexadecimal Representation.
        """
        if decimal < 0:
            raise ValueError("Negative numbers are not supported")
        return hex(decimal)[2:].upper()

    @staticmethod
    def binaryToDecimal(binary: str) -> int:
        """
        Converts a Binary Number To Decimal Representation.
        
        Args:
            binary (str): The Binary Number To Convert.
        
        Returns:
            int: The Decimal Representation.
        """
        if not all(c in '01' for c in binary):
            raise ValueError("Binary string must only contain 0's and 1's")
        return int(binary, 2)

    @staticmethod
    def binaryToHexadecimal(binary: str) -> str:
        """
        Converts a Binary Number To Hexadecimal Representation.
        
        Args:
            binary (str): The Binary Number To Convert.
        
        Returns:
            str: The Hexadecimal Representation.
        """
        decimal = NumberSystemConversion.binaryToDecimal(binary)
        return NumberSystemConversion.decimalToHexadecimal(decimal)

    @staticmethod
    def hexadecimalToDecimal(hexadecimal: str) -> int:
        """
        Converts a Hexadecimal Number To Decimal Representation.
        
        Args:
            hexadecimal (str): The Hexadecimal Number To Convert.
        
        Returns:
            int: The Decimal Representation.
        """
        if not all(c in '0123456789ABCDEF' for c in hexadecimal.upper()):
            raise ValueError("Hexadecimal string must only contain valid characters (0-9, A-F)")
        return int(hexadecimal, 16)

    @staticmethod
    def hexadecimalToBinary(hexadecimal: str) -> str:
        """
        Converts a Hexadecimal Number To Binary Representation.
        
        Args:
            hexadecimal (str): The Hexadecimal Number To Convert.
        
        Returns:
            str: The Binary Representation.
        """
        decimal = NumberSystemConversion.hexadecimalToDecimal(hexadecimal)
        return NumberSystemConversion.decimalToBinary(decimal)

class KarnaughMap:
    """
    A Class To Simplify Boolean Expressions Using Karnaugh Maps (K-map).

    Attributes:
        values (list): A List Of Boolean Values Representing The Truth Table For The Boolean Expression.
    """

    def __init__(self, values: list):
        """
        Initializes The KarnaughMap Class With A List Of Boolean Values Representing The Truth Table.

        Args:
            values (list): A List Of Boolean Values Representing The Truth Table.

        Raises:
            ValueError: If The Length Of Values Is Not 4 Or 8 (For 2-Variable or 3-Variable K-map).
        """
        if len(values) not in [4, 8]:
            raise ValueError("K-map only supports 2-variable (4 values) or 3-variable (8 values) expressions.")
        self.values = values

    def generateKmap(self) -> str:
        """
        Generates The Karnaugh Map Table For The Given Truth Table Values.

        Returns:
            str: A Neatly Formatted Karnaugh Map Table.
        """
        headers = ["00", "01", "11", "10"]  
        if len(self.values) == 8:

            headers = ["000", "001", "011", "010", "110", "111", "101", "100"]

        table = []
        for i in range(0, len(self.values), 4):
            row = self.values[i:i + 4]
            table.append(row)

        return tabulate(table, headers=headers, tablefmt="grid")

    def simplifyExpression(self) -> str:
        """
        Simplifies The Boolean Expression Using Karnaugh Map Minimization.

        Returns:
            str: The Simplified Boolean Expression.

        Raises:
            ValueError: If No Simplification Is Possible.
        """
        if len(self.values) == 4:
            return self._simplify2Variable()
        elif len(self.values) == 8:
            return self._simplify3Variable()

    def _simplify2Variable(self) -> str:
        """
        Simplifies A 2-Variable Boolean Expression Using K-map Rules.

        Returns:
            str: The Simplified Boolean Expression For 2 Variables.
        """

        simplified_expr = []
        if self.values == [1, 1, 1, 1]:
            return "1"
        elif self.values == [0, 1, 1, 0]:
            return "A"
        elif self.values == [1, 0, 0, 1]:
            return "B"

        else:
            raise ValueError("No simplification found for this expression")

    def _simplify3Variable(self) -> str:
        """
        Simplifies A 3-Variable Boolean Expression Using K-map Rules.

        Returns:
            str: The Simplified Boolean Expression For 3 Variables.
        """

        simplified_expr = []
        if self.values == [1, 1, 1, 1, 1, 1, 1, 1]:
            return "1"
        elif self.values == [0, 1, 1, 0, 1, 0, 0, 1]:
            return "A'B"

        else:
            raise ValueError("No simplification found for this expression")