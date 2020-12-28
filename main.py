import sys

numbers = []
operations = []
result = 0

def AddNumbers(number1, number2):
    return number1 + number2


def SubstractNumbers(number1, number2):
    return number1 - number2


def MultiplyNumbers(number1, number2):
    return number1 * number2


def DivideNumbers(number1, number2):
    return number1 / number2


def ModuloNumbers(number1, number2):
    return number1 % number2

try:
    numbersCount = int(input("How many numbers will you have? "))
except ValueError:
    print("Entered value is not an int number. Application will now close.\n")
    sys.exit()

if numbersCount < 2:
    print("You need at least two numbers. Application will now close")
    sys.exit()

for x in range(numbersCount):
    try:
        enteredNumber = float(input("Enter number " + str((x + 1)) + ": "))
    except ValueError:
        print("Entered value is not a number. Application will now close.\n")
        sys.exit()
        
    if x == 0:
        result = enteredNumber
        if x != numbersCount - 1:
            selectedOperation = input("Select mathematical operation (+, -, *, /, %): ")
    elif x != 0:
        if selectedOperation == "+":
            result = AddNumbers(result, enteredNumber)
        elif selectedOperation == "-":
            result = SubstractNumbers(result, enteredNumber)
        elif selectedOperation == "*":
            result = MultiplyNumbers(result, enteredNumber)
        elif selectedOperation == "/":
            result = DivideNumbers(result, enteredNumber)
        elif selectedOperation != "%":
            result = ModuloNumbers(result, enteredNumber)
        else:
            print("Invalid mathematical operation. Application will now close.\n")
            sys.exit()
            
        if x != numbersCount - 1:
            selectedOperation = input("Select mathematical operation (+, -, *, /, %): ")

print("Result = " + str(result))
