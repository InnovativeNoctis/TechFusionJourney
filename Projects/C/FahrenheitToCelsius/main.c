#include <stdio.h>

int main()
{
    /*Fahrenheit to Celsius conversion table */
    float fahrenheit, celsius;
    int lower, upper, step;
    lower = 0; /* lower limit of temperature table */
    upper = 300; /* upper limit */
    step = 20; /* step size */
    printf("Fahrenheit to Celsius conversion table\n");
    fahrenheit = lower;
    while (fahrenheit <= upper)
    {
        celsius = (5.0 / 9.0) * (fahrenheit - 32.0);
        printf("%3.0f %6.1f\n", fahrenheit, celsius);
        fahrenheit = fahrenheit + step;
    }
    return 0;
}