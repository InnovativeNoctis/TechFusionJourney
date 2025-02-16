# FairPay

## Overview
**FairPay** is a simple Python program that calculates daily salary based on work hours and hourly pay. It ensures that users do not exceed a healthy work limit (max 8 hours per day).  

## Features
- Calculates salary based on the number of hours worked and hourly wage.  
- Prevents excessive work by restricting hours beyond 8.  
- Provides error messages for invalid input (negative values, zero pay, etc.).  

## Usage
### **1. Run the Program**
Make sure you have Python 3 installed, then run:  

```bash
python fair_work.py
```

### **2. Enter Inputs**
The program will ask for:  
- **How many hours you worked today?** *(e.g., 6.5)*  
- **How much do you get paid per hour?** *(e.g., 15.75)*  

### **3. Get Your Salary**
The program will return:  
- Your total salary for the day if the input is valid.  
- A warning if you work more than 8 hours.  
- Error messages for invalid input.  

## Example Output
```
How many hours did you work today? 7
How much do you get paid per hour? 20
Your salary is 140.0.
```
or  
```
How many hours did you work today? 10
How much do you get paid per hour? 15
Too much work. You can't work for 2 extra hours on the next days.
```

## Requirements
- Python 3.x  
- No additional libraries needed  

## Future Improvements
- Add weekly/monthly salary calculation.  
- Include overtime pay calculations.  
- Create a graphical interface for easier use.  

## License
This project is free to use and modify.