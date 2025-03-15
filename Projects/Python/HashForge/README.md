# HashForge

## Overview

**HashForge** is a Python-based tool for generating hashes and performing rainbow table lookups using SHA-256 and SHA-512. It allows users to create hashes from a range of numbers or an input file and compare them against a dataset to find matches.

## Features

- Supports **SHA-256** and **SHA-512** hashing.
- Hashes a range of numbers or data from a CSV file.
- Performs **rainbow table lookups** to match hashes with original values.
- Outputs results to a CSV file.
- **Error handling** for missing files and invalid inputs.

## Installation

Ensure you have Python **3.x** installed on your system.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/InnovativeNoctis/HashForge.git
   cd HashForge
   ```

## Usage

Run the script using:

```bash
python hashforge.py
```

### Options:

1. Choose **SHA-256** or **SHA-512** hashing.
2. Select how to generate hashes:
   - A **range of numbers**.
   - **Data from a CSV file**.
   - **Both**.
3. Provide the input/output file paths.

Example:

```bash
python hashforge.py
```

*Follow the prompts to generate hashes and perform lookups.*

## File Format

### **Input CSV Example:**

| Key   | Hash Value    |
| ----- | ------------- |
| user1 | e3b0c44298... |
| user2 | 5d41402abc... |

### **Output CSV Example:**

| Key   | Original Value |
| ----- | -------------- |
| user1 | 12345          |
| user2 | NotFound       |

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

## Author

Developed by [@InnovativeNoctis](https://github.com/InnovativeNoctis).