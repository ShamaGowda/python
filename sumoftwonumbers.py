# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Input from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Calculating the sum
sum_result = add_numbers(number1, number2)

# Output the result
print("The sum of {0} and {1} is {2}".format(number1, number2, sum_result))