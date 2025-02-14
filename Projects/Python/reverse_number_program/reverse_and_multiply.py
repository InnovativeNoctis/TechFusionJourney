num = int(input("Please enter a 3-digit number: "))  # Get user input and convert it to an integer

# Extract the last digit (ones place)
reverse = num % 10

# Remove the last digit and move on to the next digit
num = (num - reverse) // 10

# Extract the second-to-last digit (tens place)
reverse2 = num % 10

# Remove the second-to-last digit and move on to the first digit
num = (num - reverse2) // 10

# Rebuild the number with reversed digits
reverse_num = ((reverse * 100) + (reverse2 * 10) + num)

# Print the reversed number multiplied by 2
print(reverse_num * 2)
