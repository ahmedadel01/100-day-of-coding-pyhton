# Calculator 

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operation ={
    '+': add,
    '-': subtract,
    '*':multiply,
    '/':divide
}

def calculator():

    num1 = float(input('What is the first number? '))
    shouldContinue = True

    while shouldContinue:
        operationSymple = input('Pick an operation: ')
        num2 = float(input('What is the next number? '))
        caluFanction = operation[operationSymple]
        answer = caluFanction(num1, num2)

        print(f"{num1} {operationSymple} {num2}  =  {answer}")

        if input(f"Type 'y' to continue cal with {answer}, or type 'n' to start new calculation: ") == 'y':
            num1 = answer
        else:
            shouldContinue = False
            calculator()

calculator()
