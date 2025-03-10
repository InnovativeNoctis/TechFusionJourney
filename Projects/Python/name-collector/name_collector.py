# Initialize an empty string to store names
names = ""

# Initialize a counter to track the number of inputs
count = 0

# Loop until 10 names are collected
while count != 10:
    # Ask the user for a name, strip spaces, and convert to lowercase
    n = input("Please enter your name: ").strip().lower()

    # Check if 'names' already has values
    if names:
        # Append the new name with a comma separator and capitalize the first letter
        names += f",{n.capitalize()}"
    else:
        # If it's the first name, just capitalize and assign it
        names = n.capitalize()

    # Increment the counter
    count += 1

# Split the names string into a list of individual names
names = names.split(",")

# Print each name on a new line
for name in names:
    print(name)