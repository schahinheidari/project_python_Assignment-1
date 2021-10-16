from math import sin, cos, tan, factorial, sqrt
import math

def function():
    op = input("Enter your function between [+, -, *, /, sin, cos, tan, ! (factorial), sqrt(/-)]: ")
    if op == "sin"or "cos"or "tan"or "!"or "sqrt"or "/-":
        calculator()
    elif op == "+" or "-" or "/" or "*":
        calculator1()
    else:
        print("error : correct your operation")


def calculator():
    op = input("repeat your function again")
    a = float(input("Enter your number: "))
    if op == "sin":
            process = math.sin(a)
            print("Enter your number : " + str(process)) 
    elif op == "cos":
            process = math.cos(a)
            print("Enter your number : " + str(process))
    elif op == "tan":
            process = math.tan(a)
            print("Enter your number : " + str(process))
    elif op == "!":
            process = math.factorial(a)
            print("Enter your number : " + str(process))
    elif op == "sqrt" or "/-":
            process = math.sqrt(a)
            print("Enter your number : " + str(process)) 

def calculator1():
    op = input("repeat your function again")
    a = float(input("Enter your first number: "))
    b = float(input("Enter your second number: "))  
    if op == "+":
            process = a + b
    elif op == "*":
            process = a * b
    elif op == "-":
            process = a - b
    elif op == "/":
        if b == 0:
                print("Error : division by 0")  
        else:
                process = a / b        
    print(process)
    again()
    


def again():
    calculate_again = input("Do you want to calculate again? y or n ===> ")
    if calculate_again.lower() == "y":
        function()
    elif calculate_again.lower() == "n":
        print("see you then!!")
    else:
        again()
function()