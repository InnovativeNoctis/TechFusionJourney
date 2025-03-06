# Rectangle Area Calculator

This program calculates the area of a rectangle based on user input for the **length** and **width**.

## Features

- Prompts the user to enter the **length** and **width** of a rectangle.
- Checks if the entered values are valid (positive numbers).
- Displays an error message if the input is invalid.
- Calculates and outputs the area of the rectangle if the input is valid.

## Requirements

- C++11 or higher compiler.

## How to Use

1. Compile the program using a C++ compiler:
   ```bash
   g++ -o rectangle_area rectangle_area.cpp
   ```

2. Run the compiled program:
   ```bash
   ./rectangle_area
   ```

3. Enter the **length** and **width** when prompted.

4. If the input is valid, the program will display the area of the rectangle. If the input is invalid (non-positive numbers or incorrect format), it will prompt an error message.

## Example

```bash
Enter the length: 5
Enter the width: 3
The area of your rectangle is 15
```

## Error Handling

- If the user enters **non-numeric** values or **non-positive** numbers, the program will display the following message:
  ```
  Invalid input! Length and width must be positive numbers.
  ```