def contains_hello(word):

    # If the input string is empty, return "NO"
    if not word:
        return "NO"

    target = "hello"  # The word we are searching for
    index = 0  # Tracks the position in "hello" we are checking

    # Iterate through each character in the input word
    for letter in word:
        # If the letter matches the current character of "hello"
        if letter == target[index]:
            index += 1  # Move to the next letter in "hello"

            # If we have found all letters of "hello" in order, return "YES"
            if index == len(target):
                return "YES"

    # If the loop completes without finding all letters in order, return "NO"
    return "NO"


# Get user input, convert it to lowercase, and remove extra spaces
word = input("Enter your word: ").lower().strip()

# Check if the word contains "hello" in order and print the result
print(contains_hello(word))