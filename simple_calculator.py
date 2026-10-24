""" This is a simple calculator that can add, subtract, divide,

multiply as well as find the square and square root of numbers"""

import math
def addition(a, b):
    print (a + b)

def subtraction(a, b):
    return a - b


def division(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("you cannot divide by zero")


def multiply(a, b):
    print ( a * b)

def sqr(a):
    print ( a * a)


def sqroot(a):
    if a < 0:
        print("Cannot calculate a real square root of a negative number!")
    else:
        print(math.sqrt(a))


def run_app():

    print("=" * 38)
    print("smart calculator.".upper())
    print("=" * 38)
    print()
    print("choose an operation: add, subtract,  multipy, divide, square, square root, end ")
    print()

    
    is_running = True

    while is_running:
        command = input(">> ").lower().strip()

        if command == "end":
            is_running = False
            continue

        elif command not in (
            "add", "subtract", "multiply",
            "divide", "square", "square root"
        ):
            print("Input a valid command")
            continue

        try:
            a = float(input("Enter your first number: "))

            if command != "square" :
                if command != "square root":
                  b = float(input("Enter your second number: "))

        except ValueError:
            print("Please enter a valid number!")
            continue

        if command == "add":
            addition(a, b)

        elif command == "subtract":
            print("Good")
            print(subtraction(a, b))
            

        elif command == "multiply":
            multiply(a, b)

        elif command == "divide":
            division(a, b)

        elif command == "square":
            sqr(a)

        elif command == "square root":
            sqroot(a)




run_app()
