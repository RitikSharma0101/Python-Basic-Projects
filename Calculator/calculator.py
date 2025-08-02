# calculator.py

# This is a simple Python calculator project
# It performs basic arithmetic operations in a loop until the user exits

# Return the sum of two numbers
def add(a,b):
    return a + b

# Return the difference of two numbers
def sub(a,b):
    return a - b

# Return the product of two numbers
def mul(a,b):
    return a * b

# Return the division result or an error if dividing by zero
def divide(a,b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a/b

def calculator():
    # Main calculator loop
    while True:
        # Display menu
        print("\nWelcome to My First Project - Calculator")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        # Get user choice
        choice = input("Enter choice (1/2/3/4/5): ")

        try:
            
            if choice in ["1","2","3","4","5"]:
                if choice == "5":
                    print("\nThanks for using the calculator. Goodbye!")
                    break

                # Get numbers from user
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                # Match the operation
                match choice:
                    case "1":
                        print(f"Result: {add(num1,num2)}")
                    case "2":
                        print(f"Result: {sub(num1,num2)}")
                    case "3":
                        print(f"Result: {mul(num1,num2)}")
                    case "4":
                        print(f"Result: {divide(num1,num2)}")
            else:
                print("Invalid choice. Please select from 1 to 5.")

        except ValueError:
            print("Invalid input. Please enter numeric values only.")

# Run the calculator
calculator()
