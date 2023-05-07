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
# Ask for user's Input Numbers
# Add a ValueError
# Print the out put
# Ask if the user's wants to try again