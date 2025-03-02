#include <iostream>  // Include the input-output stream library
#include <cmath>     // Include the cmath library for mathematical functions

int main() {
    double fnum, secnum;  // Declare two double variables for user input
    char operation;       // Declare a character variable to store the chosen operation

    // Prompt the user to enter the first number
    std::cout << "Enter the first number: ";
    std::cin >> fnum;

    // Prompt the user to enter the second number
    std::cout << "Enter the second number: ";
    std::cin >> secnum;

    // Prompt the user to choose an operation
    std::cout << "Choose and enter (^, *, /, %, +, -): ";
    std::cin >> operation;

    // Use a switch statement to perform the chosen operation
    switch(operation) {
        case '^': {  // Case for exponentiation (power)
            double power = std::pow(fnum, secnum);  // Calculate power using std::pow()
            std::cout << "Result: " << power;  // Display the result
            break;
        }
        case '*': {  // Case for multiplication
            double mul = fnum * secnum;  // Multiply the numbers
            std::cout << "Result: " << mul;  // Display the result
            break;
        }
        case '/': {  // Case for division
            if (secnum == 0) {  // Check if denominator is zero
                std::cout << "Error: Division by zero!";  // Display an error message
            } else {
                double div = fnum / secnum;  // Perform division
                std::cout << "Result: " << div;  // Display the result
            }
            break;
        }
        case '%': {  // Case for modulus operation
            if (secnum == 0) {  // Check if second number is zero
                std::cout << "Error: Modulo by zero!";  // Display an error message
            } else {
                double mod = std::fmod(fnum, secnum);  // Use std::fmod() for floating-point modulus
                std::cout << "Result: " << mod;  // Display the result
            }
            break;
        }
        case '+': {  // Case for addition
            double add = fnum + secnum;  // Add the numbers
            std::cout << "Result: " << add;  // Display the result
            break;
        }
        case '-': {  // Case for subtraction
            double sub = fnum - secnum;  // Subtract the numbers
            std::cout << "Result: " << sub;  // Display the result
            break;
        }
        default:  // Case for invalid input
            std::cout << "Error: Invalid operator!";  // Display an error message
            break;
    }

    return 0;  // Return 0 to indicate successful program execution
}
