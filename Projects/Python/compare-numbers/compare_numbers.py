# Get first number and convert into integer
first_number = int(input("Please enter the first number: "))

# Get second number and convert into integer
second_number = int(input("Please enter the second number: "))

# Check if first number is greater than second number and then print the first number
if first_number > second_number:
    print(first_number)

# Check if second number is greater than first number and then print the second number
elif first_number < second_number:
    print(second_number)

# Check if both are equal and then print the number
else:
    print(f"The numbers are equal: {first_number}")