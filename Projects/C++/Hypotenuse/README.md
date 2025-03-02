# Hypotenuse Calculator

## Description
This program calculates the hypotenuse of a right triangle using the lengths of the two other sides. It takes input from the user for the two side lengths, calculates their squares, sums them, and then computes the square root of that sum to find the hypotenuse. The result is displayed with two decimal places of precision.

This program demonstrates basic mathematical operations like squaring numbers, summing values, and calculating square roots. It also shows how to get user input and output formatted results in C++.

## Features
- User inputs the lengths of two sides of a right triangle.
- The program calculates the hypotenuse using the Pythagorean theorem:  
  \( c = \sqrt{a^2 + b^2} \)
- Output is displayed with two decimal places of precision.
- Includes an alternative method using `std::hypot()` (commented out for educational purposes).

## How It Works
1. The user is prompted to enter the lengths of the two sides of a right triangle.
2. The program calculates the square of each side using the `std::pow()` function.
3. It then sums the squares of the two sides.
4. Finally, the program calculates the hypotenuse by taking the square root of the sum using `std::sqrt()`.
5. The hypotenuse is then printed with 2 decimal places of precision.

## Usage
To use this program, simply compile and run the C++ file. When executed, the program will ask you to input the lengths of the two sides of a right triangle. Once entered, the hypotenuse will be displayed.

### Example:
```
Enter the first length: 3
Enter the second length: 4
The hypotenuse is: 5.00
```

## Compilation Instructions
1. Open a terminal or command prompt.
2. Navigate to the folder where the `hypotenuse.cpp` file is located (in the `Hypotenuse` folder).
3. Compile the program using a C++ compiler like `g++`:
   ```
   g++ hypotenuse.cpp -o hypotenuse
   ```
4. Run the resulting executable:
   - On Windows: `hypotenuse.exe`
   - On Linux/macOS: `./hypotenuse`

## Dependencies
- This program uses the C++ Standard Library, specifically:
  - `<iostream>` for input/output.
  - `<cmath>` for mathematical operations like `std::pow()` and `std::sqrt()`.

## License
This project is free to use and modify.