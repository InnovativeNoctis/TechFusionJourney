import math

# Function to count the divisors of a number
def divisor_count(n):
    div = 1  # Start from 1 (every number is divisible by 1)
    amount = 0  # To keep track of the number of divisors
    # Loop through numbers from 1 to n to check for divisibility
    while div <= n:
        if n % div == 0:  # If n is divisible by div (i.e., it's a divisor)
            amount += 1  # Increment the divisor count
        div += 1  # Move to the next number
    return amount  # Return the total number of divisors

# Function to get a valid number from the user
def get_valid_number(prompt):
    while True:
        try:
            num = int(input(prompt))  # Try to convert the input to an integer
            if num < 1:  # If the number is less than 1, it's invalid
                print("Please enter a positive integer greater than 0.")
            else:
                return num  # Return the valid number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Get the first valid number from the user
most_number = get_valid_number("Please enter the 1st number: ")
most_divisors = divisor_count(most_number)  # Get the divisor count of the first number

counter = 2  # Start the counter from 2 because we already have the first number

# Loop to input 19 more numbers (for a total of 20 numbers)
while counter <= 20:
    # Ask the user for the next valid number
    number = get_valid_number(f"Please enter the {counter}th number: ")
    divisors = divisor_count(number)  # Get the divisor count of the entered number

    # If the current number has more divisors than the current most, update the result
    if divisors > most_divisors:
        most_number = number
        most_divisors = divisors
    # If the divisors are the same, choose the larger number
    elif divisors == most_divisors:
        if number > most_number:  # In case of a tie, choose the larger number
            most_number = number
            most_divisors = divisors

    counter += 1  # Move to the next number

# After all 20 numbers have been entered, print the result
print(f"The number with the most divisors and the amount of them:\n{most_number} : {most_divisors}")