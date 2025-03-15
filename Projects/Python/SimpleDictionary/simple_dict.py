import string

def dictionary_maker(amount):
    dictionary = {}

    print("\nEnter words and their translations (separated by a space).")

    for _ in range(amount):
        while True:
            word_pair = input().strip().split(maxsplit=1)
            if len(word_pair) == 2:
                dictionary[word_pair[0].lower()] = word_pair[1]
                break
            else:
                print("Invalid input. Please enter exactly two words separated by a space.")

    print("\nEnter a sentence to translate:")
    sentence = input().strip().split()

    translated_words = []
    for word in sentence:
        clean_word = word.strip(string.punctuation).lower()
        translated_word = dictionary.get(clean_word, f"[{word}]")
        translated_words.append(translated_word)

    translation = " ".join(translated_words)
    print("\nTranslation:", translation.capitalize())

while True:
    try:
        n = int(input("Please enter the number of word pairs: "))
        if n <= 0:
            print("Number of words must be positive.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

dictionary_maker(n)
