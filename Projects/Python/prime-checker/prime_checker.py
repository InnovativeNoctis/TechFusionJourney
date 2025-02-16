import math  # Importing math module to use the sqrt function


def is_prime(n):
    """Function to check if a number is prime."""

    # Handle numbers less than 2 (not prime)
    if n < 2:
        return "Not prime"

    # Handle the special cases of 2 and 3 (both are prime)
    if n == 2 or n == 3:
        return "Prime"

    # Eliminate even numbers and multiples of 3 (except 2 and 3)
    if n % 2 == 0 or n % 3 == 0:
        return "Not prime"

    # Check divisibility starting from 5 up to √n
    i = 5
    while i <= math.sqrt(n):
        if n % i == 0:  # If n is divisible by i, it's not prime
            return "Not prime"
        i += 2  # Skip even numbers to optimize checking

    # If no divisors were found, the number is prime
    return "Prime"


# Taking user input and ensuring it's an integer
number = is_prime(int(input("Enter your number: ")))
print(number)  # Print whether the number is prime or not
