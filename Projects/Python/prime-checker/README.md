Of course! Here's your **README.md** file without emojis:  

---

### **📄 README.md**

# Prime Checker

This is a simple Python program that checks whether a given number is prime.

## How It Works
- The program takes an **integer input** from the user.
- It checks if the number is **prime** using an optimized algorithm that:
  - Eliminates numbers less than 2.
  - Quickly removes even numbers and multiples of 3.
  - Checks divisibility up to the square root of the number for efficiency.

## How to Run the Program
1. Make sure you have **Python 3** installed on your system.
2. Download or clone this repository.
3. Run the script using a terminal or command prompt:
   ```sh
   python prime_checker.py
   ```
4. Enter a number when prompted, and the program will tell you if it's prime.

## Example Usage
```
Enter your number: 11
Prime
```
```
Enter your number: 25
Not prime
```

## How the Algorithm Works
- If the number is **less than 2**, it's **not prime**.
- If the number is **2 or 3**, it's **prime**.
- If the number is **even or a multiple of 3**, it's **not prime**.
- Otherwise, it checks divisibility from `5` to `√n`, skipping even numbers for efficiency.

## License
This project is free to use and modify.