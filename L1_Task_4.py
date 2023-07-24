def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter the operator (+, -, *, /, %): ")
        num2 = float(input("Enter the second number: "))
        
        if operator in ['+', '-', '*', '/', '%']:
            result = eval(f"{num1} {operator} {num2}")
            print(f"Result: {result:.2f}")
        else:
            print("Error: Invalid operator!")

    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    calculator()
