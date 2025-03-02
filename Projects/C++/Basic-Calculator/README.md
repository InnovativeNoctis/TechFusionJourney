# Basic Calculator

## Overview

This is a simple calculator program written in C++ that allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, division, modulus, and exponentiation. The program prompts the user to enter two numbers and then select an operation to perform.

## Features

- Supports the following operations:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
  - Modulus (`%`) (using `std::fmod` for floating-point numbers)
  - Exponentiation (`^`) (using `std::pow`)
- Includes error handling for division and modulus by zero
- Uses a `switch` statement for operation selection

## Files

- **Folder:** `Basic-Calculator`
- **Main C++ file:** `calculator.cpp`

## How to Compile and Run

### Using g++ (GNU Compiler)

1. Open a terminal or command prompt.
2. Navigate to the `Basic-Calculator` folder.
3. Compile the program using:
   ```sh
   g++ calculator.cpp -o calculator
   ```
4. Run the program using:
   ```sh
   ./calculator  # On Linux/macOS
   calculator.exe  # On Windows
   ```

## Example Usage

```
Enter the first number: 5
Enter the second number: 2
Choose and enter (^, *, /, %, +, -): ^
Result: 25
```

## Notes

- The program uses `std::fmod()` for modulus calculations with floating-point numbers.
- If the user attempts to divide or use modulus by zero, an error message is displayed.
- If an invalid operator is entered, an error message is shown.

## Future Improvements

- Add support for more mathematical functions (e.g., square root, logarithm).
- Implement a loop to allow multiple calculations without restarting the program.
- Improve user input validation.

## License

This project is free to use and modify.
