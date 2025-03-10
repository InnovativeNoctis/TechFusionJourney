# Get user input and remove any leading/trailing spaces
opr = input("Enter your operation: ").strip()

# Initialize empty strings to store sorted numbers
one = ""
two = ""
three = ""

# Loop through each character in the input
for num in opr:
    if num == "3":
        three = three + "3 + "  # Append "3 + " if the character is '3'
    elif num == "2":
        two = two + "2 + "  # Append "2 + " if the character is '2'
    elif num == "1":
        one = one + "1 + "  # Append "1 + " if the character is '1'
    elif num == "+":
        pass  # Ignore the '+' symbol
    else:
        # Print error message and exit if an invalid character is found
        print("Error: Invalid input (%s)" % num)
        exit()

# Concatenate sorted numbers in order: 1s first, then 2s, then 3s
ott = one + two + three

# Remove the last " + " if it exists
if ott.endswith(" + "):
    ott = ott[:-3]  # Slice to remove the last three characters

# Print the formatted output
print(ott)