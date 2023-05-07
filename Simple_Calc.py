# Mohammad Mishal S. Noroña | BSCPE 1-5 | Simple Calculator
# Import Color Module
import colorama
from colorama import Fore, Back, Style
colorama.init()
# add introduction
print("")
print(Fore.LIGHTYELLOW_EX + "WELCOME TO SIMPLE CALCULATOR".center(40," ") )
print(Fore.LIGHTYELLOW_EX + "By: Mishal Noroña".center(40," ") )
# Addition Function
def addition(x, y):
    return x + y

# Subtraction Function
def subtraction(x, y):
    return x - y

# Multiplication Function
def multiplication(x, y):
    return x * y

# Division Fuction with ZeroDivisionError
def division(x, y):
    try: 
        return x / y
    except ZeroDivisionError:
        print(Fore.RED + "\nDivision by Zero Error")
# List down Operations
while True:
    print(Fore.WHITE + "\nList Of Operation \n")
    print("[a] Add")
    print("[s] Subtract")
    print("[m] Multiply")
    print("[d] Divide")
    # Ask for user's Input
    operation = input(Fore.BLUE + "Enter an Operation [a/s/m/d]: ")
    if operation in ("a", "s", "m", "d"):
        # Ask for user's Input Numbers
        try:
            num_input1 = float(input(Fore.LIGHTGREEN_EX + "Enter a number: "))
            num_input2 = float(input("Enter another number: "))
        # Add a ValueError
        except ValueError:
            print(Fore.RED + "Invalid Input")
            print("Enter a Numerical Value")
            continue
        # Print the output
        if operation == "a":
            print(num_input1, "+", num_input2, "=", addition(num_input1, num_input2))

        elif operation == "s":
            print(num_input1, "-", num_input2, "=", subtraction(num_input1, num_input2))

        elif operation == "m":
            print(num_input1, "*", num_input2, "=", multiplication(num_input1, num_input2))

        elif operation == "d":
            print(num_input1, "/", num_input2, "=", division(num_input1, num_input2))
        # Ask if the user's wants to try again
        more_input = input(Fore.LIGHTCYAN_EX + "Do you want to Enter another? (y/n): ")
        if more_input == "y":  
            continue
        elif more_input == "n":
            print(Fore.CYAN + "Thank you for using Simple Calculator")
            break
        else:
            print(Fore.RED + "\nInvalid Input")
            break