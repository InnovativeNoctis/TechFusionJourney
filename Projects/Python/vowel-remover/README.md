# vowel_remover

## **Description**
`vowel_remover.py` is a Python script that processes an input string by:
1. Removing all vowels (a, e, i, o, u) from the string.
2. Adding a dot (`.`) before each consonant.

The result is a string where consonants are preceded by a dot, and vowels are removed. Spaces, punctuation marks, and other non-alphabetic characters are **not included** in the final output.

## **Features**
- Removes vowels from the input string.
- Adds a dot before every consonant.
- Converts the string to lowercase for uniform processing.
- Skips non-alphabetic characters (spaces, punctuation, etc.) and they are not included in the output.

## **How to Use**

1. Clone or download the repository.
2. Run the script in your Python environment.

```bash
python vowel_remover.py
```

3. The script will prompt you to enter a string. After entering the string, it will:
   - Remove all vowels (`a, e, i, o, u`).
   - Add a dot (`.`) before each consonant.
   - Skip non-alphabetic characters (e.g., punctuation, spaces), which will not be included in the output.

## **Example**

### Input:
```
Enter your strings: Hello World!
```

### Output:
```
.h.l.l.w.r.l.d
```

## **Requirements**
- Python 3.x

## License
This project is free to use and modify.