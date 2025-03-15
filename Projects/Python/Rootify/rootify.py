import math  # Import the math module to use sqrt function


def compute_sqrt(amount):
    """Function to collect 'amount' numbers from the user and compute their square roots."""

    numbers = []  # List to store the user-input numbers

    # Loop to collect the required number of inputs
    for _ in range(amount):
        while True:
            try:
                n = float(input("Enter a number: "))  # Prompt user for input
                numbers.append(n)  # Add valid number to the list
                break  # Exit the loop if input is valid
            except ValueError:
                print("Error: Invalid value. Enter a number.")  # Error handling for non-numeric input

    # Display the computed square roots
    print("\nSquare roots of your numbers:")
    for n in numbers:
        print(f"√{n} = {math.sqrt(n):.5f}")  # Display square root with 5 decimal places


# Loop to validate user input for the number of values
while True:
    try:
        a = int(input("Enter the amount of numbers that you want to enter: "))
        if a < 1:
            print("Invalid integer. Minimum is one.")  # Ensure at least one number is entered
        else:
            break  # Valid input, exit loop
    except ValueError:
        print("Error: Invalid value. Enter an integer.")  # Error handling for non-integer input

print("\nPlease enter each of your numbers and then hit enter.")  # User guidance
compute_sqrt(a)  # Call the function to compute square roots