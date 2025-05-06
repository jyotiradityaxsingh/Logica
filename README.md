![Banner](Resources/Banner%20(Logica).png)


# Logica

This Program Is Designed To Help With **Digital Electronics**, Making It Easier To Learn And Apply Digital Electronics Concepts

---

## Features

### 1. Boolean Algebra Operations

The **BooleanAlgebra** Class Allows You To Perform Various Logical Operations On Two Boolean Values. The Available Logic Gates Include:
- **NOT** (Inverts A Value)
- **AND** (Returns `True` If Both Values Are `True`)
- **OR** (Returns `True` If Either Value Is `True`)
- **NAND** (Returns `True` If Not Both Values Are `True`)
- **NOR** (Returns `True` If Both Values Are `False`)
- **XOR** (Returns `True` If Exactly One Value Is `True`)
- **XNOR** (Returns `True` If Both Values Are The Same)

### 2. Binary Operations

The **BinaryOperations** Class Provides Methods To Perform Basic Binary Arithmetic Operations:
- **Addition**
- **Subtraction**
- **Multiplication**
- **Division**

All Binary Operations Are Performed Step-By-Step, Showing Intermediate Results For Better Understanding.

---

## Installation

To Use This Program, Simply Clone The Repository And Run The Python File:

```bash
git clone https://github.com/yourusername/digital-electronics-assistant.git
cd digital-electronics-assistant
python main.py
```

---

## Usage

### Running The Application
Once The Program Is Executed, You Will Be Presented With A Menu To Choose Between **Boolean Algebra** And **Binary Operations**:

```bash
Commands:

1> Boolean Algebra (Using Two Values)
2> Binary Operations (Addition, Subtraction, Multiplication, And Division)
```

#### Boolean Algebra Operations
- Select **1** To Choose Boolean Algebra Operations.
- Input Two Boolean Values (Either `True` Or `False`).
- Select The Desired Logic Gate (1-7) From The Available Options.

#### Binary Operations
- Select **2** To Choose Binary Operations.
- Choose The Type Of Binary Operation (Addition, Subtraction, Multiplication, Or Division).
- Input Two Integers For The Operation.
- The Program Will Show Intermediate Steps For Addition, Subtraction (Using Two's Complement), Multiplication (Using Shift-And-Add), And Division (Quotient And Remainder).

---

## Example

### Boolean Algebra Example:
```bash
Enter Value One (Either True Or False)> True
Enter Value Two (Either True Or False)> False
Choose The Logic Gate (1-7): 2
```
**Output**:
```
Result Of AND Gate: False
```

### Binary Operations Example:
```bash
Enter Operation> 1
Enter Value One> 5
Enter Value Two> 3
```
**Output**:
```
Performing Binary Addition: 101 + 11
Result (Binary): 1000
```

## Contributing

Feel Free To Fork The Repository, Submit Issues, And Open Pull Requests. We Welcome Contributions To Improve The Program!

---

## License

This Program Is Licensed Under The MIT License - See The [LICENSE](LICENSE) File For Details.

---
