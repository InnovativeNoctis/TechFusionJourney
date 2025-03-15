# GPA Calculator

This Python script reads student grades from a CSV file, calculates their GPAs, and writes the results to an output CSV file. It includes functions to:

- Calculate the GPA for each student.
- Sort students based on their GPA.
- Find the top 3 students.
- Find the bottom 3 students.
- Calculate the overall average GPA.

## Usage
1. Prepare an input CSV file with student names and their grades, e.g.:
   ```csv
   Alice,80,90,85
   Bob,75,60,70
   Charlie,95,100,98
   ```

2. Run the script and provide the input and output file names when prompted.
   ```sh
   python calculate_gpa.py
   ```

3. The output file will contain the calculated GPAs, sorted lists, and summaries.

## Requirements
- Python 3
- `csv` module (built-in)
- `statistics` module (built-in)

## License
This project is open-source and free to use.