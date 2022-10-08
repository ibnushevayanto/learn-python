def add(n1, n2):
    return n1 + n2
def substract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2 
def divide(n1, n2):
    return n1 / n2
def operationFunc(n1, n2, operation):
    if operation == "+":
        return add(n1, n2)
    elif operation == "-":
        return substract(n1, n2)
    elif operation == "*":
        return multiply(n1, n2)
    elif operation == "/":
        return divide(n1, n2)

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}
while True: 
    result = float(input("What is the first number: "))

    while True:
        for keyOperation in operations:
            print(keyOperation)
            
        operation = input("Pick an operation: ")
        nextNumber = float(input("What is the next number: "))
        hasilHitung = operationFunc(result, nextNumber, operation)
        
        print(f"{round(result)} {operation} {round(nextNumber)} = { round(hasilHitung)}")
        result = hasilHitung
    
        isContinue = input(f"Type 'y' to continue calculating with {result} 'n' to start new calculation: ").lower()

        if isContinue != "y":
            break

    
    