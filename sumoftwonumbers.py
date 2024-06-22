# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Main program
if __name__ == "__main__":
    # Ask the user for input
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        
        # Add the numbers
        result = add_numbers(number1, number2)
        
        # Print the result
        print(f"The sum of {number1} and {number2} is {result}")
    
    except ValueError:
        print("Invalid input! Please enter numeric values.")