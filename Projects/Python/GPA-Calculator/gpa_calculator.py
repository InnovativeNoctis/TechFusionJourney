import csv
from statistics import mean 

# Function to calculate the average GPA for each student and save it to a CSV file
def calculate_averages(input_file_name, output_file_name):
    gpa_list = {}
    with open(input_file_name, "r") as rfile:
        reader = csv.reader(rfile)
        for row in reader:
            grades = [float(x) for x in row[1:]]  # Convert grades to float
            gpa_list[row[0]] = round(mean(grades), 3)  # Calculate mean GPA

    with open(output_file_name, "w", newline="") as wfile:  # Write mode ("w")
        writer = csv.writer(wfile)
        writer.writerow(["Student", "GPA"])  # Add header
        for key, value in gpa_list.items():
            writer.writerow([key, value])

# Function to calculate and sort the GPAs in descending order
def calculate_sorted_averages(input_file_name, output_file_name):
    gpa_list = {}
    with open(input_file_name, "r") as rfile:
        reader = csv.reader(rfile)
        for row in reader:
            grades = [float(x) for x in row[1:]]
            gpa_list[row[0]] = round(mean(grades), 3)

    sorted_gpa_list = sorted(gpa_list.items(), key=lambda item: item[1], reverse=True)

    with open(output_file_name, "a", newline="") as wfile:  # Append mode ("a")
        writer = csv.writer(wfile)
        writer.writerow([])  # Empty row for separation
        writer.writerow(["Sorted Student", "GPA"])
        for skey, svalue in sorted_gpa_list:
            writer.writerow([skey, svalue])

# Function to get the top 3 students based on GPA
def calculate_three_best(input_file_name, output_file_name):
    gpa_list = {}
    with open(input_file_name, "r") as rfile:
        reader = csv.reader(rfile)
        for row in reader:
            grades = [float(x) for x in row[1:]]
            gpa_list[row[0]] = round(mean(grades), 3)

    sorted_gpa_list = sorted(gpa_list.items(), key=lambda item: item[1], reverse=True)[:3]

    with open(output_file_name, "a", newline="") as wfile:
        writer = csv.writer(wfile)
        writer.writerow([])
        writer.writerow(["Top 3 Students", "GPA"])
        for skey, svalue in sorted_gpa_list:
            writer.writerow([skey, svalue])

# Function to get the bottom 3 students based on GPA
def calculate_three_worst(input_file_name, output_file_name):
    gpa_list = {}
    with open(input_file_name, "r") as rfile:
        reader = csv.reader(rfile)
        for row in reader:
            grades = [float(x) for x in row[1:]]
            gpa_list[row[0]] = round(mean(grades), 3)

    sorted_gpa_list = sorted(gpa_list.items(), key=lambda item: item[1])[:3]

    with open(output_file_name, "a", newline="") as wfile:
        writer = csv.writer(wfile)
        writer.writerow([])
        writer.writerow(["Bottom 3 Students", "GPA"])
        for skey, svalue in sorted_gpa_list:
            writer.writerow([skey, svalue])

# Function to calculate the average of all students' GPAs
def calculate_average_of_averages(input_file_name, output_file_name):
    all_gpas = []

    with open(input_file_name, "r") as rfile:
        reader = csv.reader(rfile)
        for row in reader:
            grades = [float(x) for x in row[1:]]
            all_gpas.append(mean(grades))

    mean_all_gpas = {"Average": f"{mean(all_gpas):.3f}"}

    with open(output_file_name, "a", newline="") as wfile:
        writer = csv.writer(wfile)
        writer.writerow([])
        writer.writerow(["Metric", "Value"])
        for key, value in mean_all_gpas.items():
            writer.writerow([key, value])

# User input for file names
input_file = input("Enter your input CSV file: ")
output_file = input("Enter your output CSV file: ")

# Calling all functions in sequence to ensure output is written correctly
calculate_averages(input_file, output_file)
calculate_sorted_averages(input_file, output_file)
calculate_three_best(input_file, output_file)
calculate_three_worst(input_file, output_file)
calculate_average_of_averages(input_file, output_file)