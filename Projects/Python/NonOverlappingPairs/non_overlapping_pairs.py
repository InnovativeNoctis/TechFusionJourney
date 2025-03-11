def checker(w):
    w = w.strip().lower()
    ab_index = -1  # Store last seen "AB" index
    ba_index = -1  # Store last seen "BA" index

    index = 0
    while index < len(w) - 1:  # Check to see if index is not out of range
        combination = w[index] + w[index + 1]

        if combination == "ab":
            if ba_index != -1 and ba_index < index - 1:
                return "YES"
            ab_index = index
            index += 2  # Move forward to avoid overlap
        elif combination == "ba":
            if ab_index != -1 and ab_index < index - 1:
                return "YES"
            ba_index = index
            index += 2  # Move forward to avoid overlap
        else:
            index += 1  # Move forward normally

    return "NO"


word = input("Enter your word: ") # Get the word
print(checker(word)) # print the result