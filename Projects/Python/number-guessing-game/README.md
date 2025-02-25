# Guess the Number Game

This is a simple number guessing game where the program tries to guess the number you're thinking of based on your inputs.

## How to Play

1. The program will start by asking if a randomly generated number is your number.
2. You will respond with one of the following:
   - `G`: If the number is greater than your number.
   - `S`: If the number is smaller than your number.
   - `T`: If the number is correct.
3. The program will continue adjusting the range based on your responses and keep guessing until it finds the correct number.

## Requirements

- Python 3.x

## How to Run the Game

1. Clone or download the repository to your local machine.
2. Open a terminal and navigate to the folder containing the game.
3. Run the Python file:

   ```bash
   python guess_the_number.py
   ```

## Example

```
Please pick a number between 1 - 99 and hold it in your memory.
Enter `G` if the number is greater than your number.
Enter `S` if the number is smaller than your number.
Enter `T` if it's the right number.

Is it 25? S
Is it 84? G
Is it 69? S
Is it 73? G
Is it 71? S
Is it 71? T
Your number after 6 attempts: 71
```

## License
This project is free to use and modify.