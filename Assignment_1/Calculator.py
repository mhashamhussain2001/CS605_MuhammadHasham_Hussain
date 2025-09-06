# Defining operation functions. 
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Error: Can't divide by 0"
    return a / b

# Welcome screen
print("Welcome to the Simple Calculator")

# While True loop used to loop the process again unless the user gives selects the option to stop.
while True: 
    # Following loop handles number input, and gracefully handles incorrect input.
    while True:
        try:
            a = float(input("First number: "))
            b = float(input("Second number: "))
            break   
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    # Following loop handles operation input and gracefully handles incorrect input.
    while True:
        print("Select an operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
        option = input("Enter the operation number: ")

        if option == "1":
            print(add(a,b))
            break
        elif option == "2":
            print(subtract(a,b))
            break
        elif option == "3":
            print(multiply(a,b))
            break
        elif option == "4":
            print(divide(a,b))
            break
        else:
            print("Invalid choice, please select 1, 2, 3, or 4.")

    # All of the calculator input, operations and output are subject to the repeating because of the while true loop in line 20
    while True:
        repeat = input("Do you want to perform another calculation? (y/n): ")
        if repeat in ("y"):
            break
        elif repeat in ("n"):
            print("Goodbye!")
            exit()
        else:
            print("Incorrect input, please use 'y' or 'n'.")