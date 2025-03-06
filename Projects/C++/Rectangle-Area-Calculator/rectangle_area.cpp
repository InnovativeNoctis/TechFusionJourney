#include <iostream>
#include <string>

int main (){
    double length;
    double width; 

    std::cout << "Enter the length: ";
    std::cin >> length ;
    
    std::cout << "Enter the width: ";
    std::cin >> width;

    if (std::cin.fail() || length <= 0 || width <= 0 ) {
        std::cout << "Invalid input! Length and width must be positive numbers." << std::endl;
        return 1;
    }

    std::cout << "The area of your rectangle is " << length*width << std::endl;
    return 0;
}