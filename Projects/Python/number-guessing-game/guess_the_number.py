import random  # Import the random module to generate random numbers

# Generate a random target number between 1 and 99
target_number = random.randint(1, 99)

# Instructions for the user on how to respond
print("Please pick a number between 1 - 99 and hold it in your memory.")
print("Enter `G` if the number is greater than your number.")
print("Enter `S` if the number is smaller than your number.")
print("Enter `T` if it's the right number.")

# Ask the user if the target number is their number
guess = input(f"Is it {target_number}? ")

# Set the lower and upper bounds for the number range
small = 1
great = 99

# Start the attempt counter
attempt = 1

# Loop while the guess isn't correct (T for correct)
while guess.lower() != "t":
    # If the guess is "G", the number is greater than the target number
    if guess.lower() == "g":
        great = target_number  # Adjust the upper bound to the current target number
    # If the guess is "S", the number is smaller than the target number
    elif guess.lower() == "s":
        small = target_number  # Adjust the lower bound to the current target number
    # If the input is neither G, S, nor T, ask the user to enter a valid answer
    else:
        print("Invalid answer. Please choose between (G/S/T).")
        guess = input(f"Is it {target_number}? ")  # Ask again for a valid answer
        continue  # Skip the rest of the loop and ask for input again

    # After adjusting the range, pick a new random number within the new bounds
    if small < great:  # Only generate a number if the range is valid
        target_number = random.randint(small, great)
    else:
        print("Something went wrong with the number range. Please restart the game.")
        break

    # Increment the attempt counter
    attempt += 1

    # Ask the user again if the new target number is their number
    guess = input(f"Is it {target_number}? ")

# After the loop, check if the correct number was guessed in the first attempt
if guess.lower() == "t":
    if attempt == 1:
        print(f"Your number after {attempt} attempt: {target_number}")
    else:
        print(f"Your number after {attempt} attempts: {target_number}")
