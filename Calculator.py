logo = """ 
_____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

WELCOME TO THE CALCULATOR!

"""
print(logo)

def add(n1, n2):
    return n1+n2
def subtract(n1, n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
def modulo(n1, n2):
    return n1%n2

operations = {
    '+': add, 
    '-': subtract, 
    '*': multiply, 
    '/': divide, 
    '%': modulo,
}

def calculator():
    to_continue = True
    num1 = float(input("what is the first number?: "))
    while to_continue:


        for symbol in operations:
            print(symbol)
        operator = input("Pick an operation: ")
        num2 = float(input("what is the next number?: "))
        res = operations[operator](num1, num2)
        print(res)

        choice = input("Type 'y' to continue or type 'n' to start new: ").lower()
        if choice == 'y':
            num1 = res
        else:
            to_continue = False
            print("\n"*10)
            calculator()
        
calculator()


 

    
