import art
import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,}

def calculator():
    os.system('clear')
    print(art.logo)
    more = "y"
    
    num1 = float(input("What's the first number? "))
    
    for symbol in operators:
        print(symbol, end = "   ")
    while more == "y":
        operator_symbol = input("\nPick an operation: ")
        
        num2 = float(input("What's the next number? "))
            
        calculate = operators[operator_symbol]
        
        answer = calculate(num1, num2)
        print(f"{num1} {operator_symbol} {num2} = {answer}")
        more = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.")
        if more == 'y':
            num1 = answer
        else:
            calculator()

calculator()