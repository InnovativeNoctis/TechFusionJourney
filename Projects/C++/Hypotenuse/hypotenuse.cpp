#include <iostream>  // Include the I/O library for input and output operations
#include <cmath>     // Include the cmath library for mathematical functions like sqrt and pow

int main(){
    
    double flength;  // Declare a variable to store the first length
    double seclength;  // Declare a variable to store the second length
    
    // Ask the user to input the first length
    std::cout << "Enter the first length: ";
    std::cin >> flength;  // Read the user's input and store it in flength

    // Ask the user to input the second length
    std::cout << "Enter the second length: ";
    std::cin >> seclength;  // Read the user's input and store it in seclength

    // Calculate the square of the first side using std::pow()
    double firstSideSquared = std::pow(flength, 2);  
    
    // Calculate the square of the second side using std::pow()
    double secondSideSquared = std::pow(seclength, 2);
    
    // Sum the squares of both sides
    double sum = firstSideSquared + secondSideSquared;
    
    // Calculate the hypotenuse by taking the square root of the sum
    double hypotenuse = std::sqrt(sum);

    // Output the hypotenuse, with precision of 2 decimal places
    std::cout.precision(2);  // Set precision to 2 decimal places
    std::cout << std::fixed;  // Ensure the output is in fixed-point notation
    std::cout << "The hypotenuse is: " << hypotenuse << std::endl;
    
    // Alternative method (commented out), using std::hypot() to calculate the hypotenuse directly
    /* 
    double hypotenuse = std::hypot(flength, seclength); 
    But I just wanted to make sure that I have learned what I have studied. 
    */

    return 0;  // Return 0 to indicate the program executed successfully
}