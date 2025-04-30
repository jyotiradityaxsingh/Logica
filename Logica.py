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

# Example usage:
truth_table = TruthTables(True, False)
print(truth_table.generate_truth_table())
