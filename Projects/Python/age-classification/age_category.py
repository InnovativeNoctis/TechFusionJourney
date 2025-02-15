age = int(input("Enter your age: "))

# Ask the user to input their age
age = int(input("Enter your age: "))

# Check if the age is in the toddler range (0-3 years old)
if 0 <= age <= 3:
    print("You are a toddler (0-3 years old).")

# Check if the age is in the child range (4-12 years old)
elif 4 <= age <= 12:
    print("You are a child (4-12 years old).")

# Check if the age is in the teenager range (13-19 years old)
elif 13 <= age <= 19:
    print("You are a teenager (13-19 years old).")

# Check if the age is in the young adult range (20-35 years old)
elif 20 <= age <= 35:
    print("You are a young adult (20-35 years old).")

# Check if the age is in the adult range (36-55 years old)
elif 36 <= age <= 55:
    print("You are an adult (36-55 years old).")

# Check if the age is in the middle-aged range (56-65 years old)
elif 56 <= age <= 65:
    print("You are middle-aged (56-65 years old).")

# Check if the age is in the senior range (65+ years old)
elif age >= 66:
    print("You are a senior (65+ years old).")

# If the user enters an invalid age (negative number)
else:
    print("Invalid age entered. Please enter a non-negative number.")
