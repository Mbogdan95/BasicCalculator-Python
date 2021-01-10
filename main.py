# Created at 28-Dec-2020

import sys

# Defining variable
result = 0

# *Method to add two numbers 
def AddNumbers(number1, number2):
    return number1 + number2

# *Method to substract two numbers
def SubstractNumbers(number1, number2):
    return number1 - number2

# *Method to multiply two numbers
def MultiplyNumbers(number1, number2):
    return number1 * number2

# *Method to divide two numbers
def DivideNumbers(number1, number2):
    return number1 / number2

# * Method to get the reminder between two numbers
def ModuloNumbers(number1, number2):
    return number1 % number2

# Try/catch to check input type
try:
    # Get how many numbers will be used
    numbersCount = int(input("How many numbers will you have? "))
except ValueError:
    # Show error to user
    print("Entered value is not an int number. Application will now close.\n")
    # Exit application
    sys.exit()

# Check if user will use more than two numbers
if numbersCount < 2:
    # Show error to user
    print("You need at least two numbers. Application will now close")
    # Exit application
    sys.exit()

# Iterate through how many numbers will be used
for x in range(numbersCount):
    try:
        # Get number from user
        enteredNumber = float(input("Enter number " + str((x + 1)) + ": "))
    except ValueError:
        # Show error to user
        print("Entered value is not a number. Application will now close.\n")
        # Exit application
        sys.exit()
        
    # Check if it's first number or not
    if x == 0:
        # Set result as the entered number
        result = enteredNumber
        # Check if number is not the last one
        if x != numbersCount - 1:
            # Get mathematical operation from user
            selectedOperation = input("Select mathematical operation (+, -, *, /, %): ")
    elif x != 0:
        # Check the mathematical operation
        if selectedOperation == "+":
            # Set result as result from method
            result = AddNumbers(result, enteredNumber)
        elif selectedOperation == "-":
            # Set result as result from method
            result = SubstractNumbers(result, enteredNumber)
        elif selectedOperation == "*":
            # Set result as result from method
            result = MultiplyNumbers(result, enteredNumber)
        elif selectedOperation == "/":
            # Set result as result from method
            result = DivideNumbers(result, enteredNumber)
        elif selectedOperation != "%":
            # Set result as result from method
            result = ModuloNumbers(result, enteredNumber)
        else:
            # Show error if mathematical operation the user set is valid
            print("Invalid mathematical operation. Application will now close.\n")
            # Exit application
            sys.exit()
            
        # Check if number is not the last one
        if x != numbersCount - 1:
            # Get mathematical operation from user
            selectedOperation = input("Select mathematical operation (+, -, *, /, %): ")

# Show result to user
print("Result = " + str(result))
