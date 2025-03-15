import csv
import os
from hashlib import sha256, sha512

def hash_maker(sha_type, number_range=None, input_file=None):
    """
    Generates a dictionary of hashes using SHA-256 or SHA-512.
    
    Parameters:
        sha_type (int): 1 for SHA-256, 2 for SHA-512
        number_range (tuple): A range of numbers to hash (start, end)
        input_file (str): Path to a CSV file containing data to hash
    
    Returns:
        dict: A dictionary where keys are hashed values and values are original data
    """
    hash_dict = {}  # Dictionary to store hashes
    
    # Select hash function based on user input
    hash_function = sha256 if sha_type == 1 else sha512

    # Generate hashes for a range of numbers if provided
    if number_range is not None:
        start, end = number_range
        for num in range(start, end + 1):  # Loop from start to end (inclusive)
            hash_dict[hash_function(str(num).encode()).hexdigest()] = str(num)

    # Generate hashes from an input file if provided
    if input_file is not None:
        try:
            with open(input_file, "r", newline="") as rfile:
                reader = csv.reader(rfile)
                for row in reader:
                    if row:  # Ensure row is not empty
                        hash_dict[hash_function(row[0].encode()).hexdigest()] = row[0]
        except FileNotFoundError:
            print(f"Error: File '{input_file}' not found.")
            return {}

    return hash_dict

def rainbow_hash(input_file, output_file, hash_dict):
    """
    Reads an input file, checks if values exist in the precomputed hash dictionary,
    and writes the results to an output file.

    Parameters:
        input_file (str): Path to the input CSV file (key-value pairs)
        output_file (str): Path to save the output file
        hash_dict (dict): Dictionary mapping hashes to original values
    """
    dict_file = {}  # Dictionary to store key-value pairs from input file
    
    # Read input CSV file
    try:
        with open(input_file, "r", newline="") as rfile:
            reader = csv.reader(rfile)
            for row in reader:
                if len(row) >= 2:  # Ensure row has at least two columns
                    dict_file[row[0]] = row[1]
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return

    # Write matched hash values to output file
    with open(output_file, "w", newline="") as wfile:
        writer = csv.writer(wfile)
        for key, value in dict_file.items():
            writer.writerow([key, hash_dict.get(value, "NotFound")])  # Write "NotFound" if value is missing

def main():
    """
    Main function that interacts with the user to get inputs and process hashing.
    """
    try:
        # Prompt user to choose hash type
        sha_type = int(input("(1)SHA-256, (2)SHA-512: "))
        if sha_type not in (1, 2):
            raise ValueError("Invalid SHA type selection.")

        # Prompt user to choose how to generate hashes
        hash_maker_type = int(input("(1)Range of numbers, (2)Input file to hash, (3)Both: "))

        numbers_range, path = None, None

        # Handle number range input
        if hash_maker_type == 1 or hash_maker_type == 3:
            numbers_range = input("Enter the number range (start,end): ").split(",")
            numbers_range = [int(numbers_range[0]), int(numbers_range[1])]

        # Handle file input
        if hash_maker_type == 2 or hash_maker_type == 3:
            path = input("Enter your file path: ").strip()
            if not os.path.exists(path):  # Validate file existence
                print("Error: File does not exist.")
                return
        
        # Prompt for input and output file paths
        input_file = input("Enter the input file path: ").strip()
        output_file = input("Enter the output file path: ").strip()

        # Generate hash dictionary and perform hash matching
        hash_dict = hash_maker(sha_type, numbers_range, path)
        rainbow_hash(input_file, output_file, hash_dict)

        print(f"Output saved to {output_file}")

    except ValueError as e:
        print(f"Input Error: {e}")

# Run the script only if it's executed directly
if __name__ == "__main__":
    main()