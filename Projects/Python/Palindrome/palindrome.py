def checker(w):
    reverse = w[::-1] # reverses the word
    if reverse == w: # if it is a palindrome
        return "palindrome"
    else: #if it is not
        return "not palindrome"


word = input("Enter your word: ").strip() # gets the word and remove spaces
print(checker(word)) # uses the function and prints the result