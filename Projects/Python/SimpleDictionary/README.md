# **Dictionary Translator**  

## **Overview**  
This Python script allows users to create a simple dictionary of word translations and use it to translate a sentence.  

## **How It Works**  
1. Enter the number of word pairs you want to add.  
2. Input each word along with its translation (separated by a space).  
3. Enter a sentence to translate using the words in your dictionary.  
4. The program will output the translated sentence.  
5. If a word is not found in the dictionary, it will be shown in brackets `[word]`.  

## **Example Usage**  
### **Input:**  
```
Please enter the number of word pairs: 3  

Enter words and their translations (separated by a space).  
hello bonjour  
world monde  
friend ami  

Enter a sentence to translate:  
Hello, my friend!  
```
### **Output:**  
```
Translation: Bonjour, my ami!
```

## **Features**  
- Case-insensitive word matching  
- Handles punctuation in sentences  
- Indicates missing words with brackets `[word]`  
- Prevents incorrect input formatting  

## **How to Run**  
Ensure you have **Python 3** installed. Then, run the script:  
```bash
python3 dictionary_translator.py
```
For Windows users, you may need to use:  
```powershell
python dictionary_translator.py
```

## **License**  
This script is free to use and modify.