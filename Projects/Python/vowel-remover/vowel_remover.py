# Take input from the user
text = input("Enter your strings: ")

# Convert the text to lowercase to make the vowel check case-insensitive
text = text.lower()

# Step 1: Remove all vowels from the input string
new_text = ""  # Initialize an empty string to store the consonants
for letter in text:
    # If the letter is not a vowel (not in 'aeiou'), add it to the new_text string
    if letter not in "aeiou":
        new_text += letter

# Step 2: Add a dot before each consonant
result = ""  # Initialize an empty string to store the final result
for letter in new_text:
    # Check if the character is a letter (to avoid adding a dot before spaces or other symbols)
    if letter.isalpha():
        # Add a dot before each letter (consonant) and append it to the result string
        result += f".{letter}"

# Print the final result
print(result)
