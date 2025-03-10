def checker(w):
    # Initialize counters for uppercase and lowercase letters
    cap = 0
    low = 0

    # Iterate through each letter in the string
    for l in w:
        # Check if the letter is uppercase
        if l == l.upper():
            cap += 1  # Increment the uppercase counter
        else:
            low += 1  # Increment the lowercase counter

    # If there are more uppercase letters than lowercase, convert the whole string to uppercase
    if cap > low:
        return w.upper()
    else:
        # Otherwise, convert the whole string to lowercase
        return w.lower()

# Prompt the user for a word and remove any leading/trailing spaces
word = input("Enter the word:").strip()

# Print the result based on the checker function
print(checker(word))