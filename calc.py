

def add(n1, n2):
    return  n1 + n2

def sub(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def div(n1,n2):
    return n1/n2

operations = {

    "+":add,
    "-":sub,
    "*":multiply,
    "/":div

}

def calculator():

    num1 = float(input("What is the first number? "))

    for operation in operations:
        print(operation)

    should_continue = True

    while should_continue:

        operation_symbol = input("Pick an operation")

        num2 = float(input("What is the next number? "))

        calc_function = operations[operation_symbol]

        result = calc_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        continuation_answer = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation")

        if continuation_answer == "y":
            num1 = result
        else:
            should_continue = False
            calculator()

calculator()