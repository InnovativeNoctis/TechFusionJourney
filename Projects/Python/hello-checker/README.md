# HelloChecker  

HelloChecker is a simple Python script that checks if the word **"hello"** appears in order within a given input string.  
The letters must be in order, but they do **not** need to be consecutive.  

## How to Run  

1. Navigate to the **Python** folder
   
2. Run the script:  
   ```bash
   python hello_checker.py
   ```

## Example Usage  

```bash
Enter your word: hxbeyldflo
YES
```

```bash
Enter your word: hlleo
NO
```

## Code Explanation  

- The function **`contains_hello(word)`** checks for the sequence `"hello"`.  
- It **iterates** through the input string and keeps track of how many letters of `"hello"` appear in order.  
- If all letters are found in sequence, it returns `"YES"`, otherwise `"NO"`.  

## Features  

- Simple and efficient string checking  
- Ignores extra letters but keeps the correct order  
- Case-insensitive input handling  

## License  

This project is open-source and available under the **MIT License**.