# Sort Numbers Program

## Description
This is a simple Python program that takes a mathematical operation consisting of numbers (`1`, `2`, and `3`) separated by `+` signs, sorts the numbers in ascending order, and outputs the formatted result.

## Features
- Accepts input in the form of numbers separated by `+` (e.g., `3+2+1+3+2`).
- Sorts the numbers in ascending order.
- Outputs the sorted numbers with `+` in between.
- Handles invalid input by displaying an error message and exiting.

## How It Works
1. The program asks the user to enter an operation.
2. It loops through each character in the input:
   - If it is `1`, `2`, or `3`, it stores it.
   - If it is `+`, it is ignored.
   - If it is an invalid character, an error message is displayed, and the program exits.
3. The stored numbers are concatenated in sorted order.
4. Any trailing `+` is removed before displaying the final result.

## Usage
Run the script and enter an operation when prompted:
```
Enter your operation: 3+2+1+3+2
1 + 2 + 2 + 3 + 3
```

### Example Outputs
#### Valid Input
```
Enter your operation: 3+1+2+3
1 + 2 + 3 + 3
```

#### Invalid Input
```
Enter your operation: 3+5+2
Error: Invalid input (5)
```

This project is part of my Python learning journey!