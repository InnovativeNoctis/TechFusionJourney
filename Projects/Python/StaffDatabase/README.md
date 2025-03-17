# StaffDatabase

**StaffDatabase** is a Python project that interacts with a MySQL database to manage and store staff (or team) data. The project allows users to create a database, create tables, add employee records, and view stored data. It serves as an efficient way to manage and organize staff information such as name, age, height, and weight.

## Features

- **Create Database**: Connects to MySQL and creates a new database if it doesn't exist.
- **Create Table**: Creates a table to store employee data (name, weight, height).
- **Add Employee**: Inserts new employee records into the table.
- **Check Staff**: Retrieves and displays all employee data stored in the database.

## Installation

1. **Install MySQL**: Make sure MySQL is installed and running on your machine. You can follow the [MySQL installation guide](https://dev.mysql.com/doc/refman/8.0/en/installing.html).
   
2. **Install Python**: Ensure Python 3 is installed on your system. You can download it from the official website: https://www.python.org/downloads/.

3. **Install Required Libraries**: Install the required Python libraries using `pip`:
   ```bash
   pip install mysql-connector-python
   ```

4. **Setup MySQL**:
   - Create a MySQL user and grant privileges if needed.
   - Ensure the database exists or will be created by the script.

## Usage

### 1. **Create a Database**
   Use the function `Create_Database()` to connect to the MySQL server and create a new database:
   ```python
   Create_Database(host, user, password, database)
   ```

### 2. **Create a Table**
   Use the function `Create_Table()` to create a table that will store the employee's data:
   ```python
   Create_Table(host, user, password, database)
   ```

### 3. **Add an Employee**
   Insert a new employee's data (name, height, weight) into the table using `Add_Employee()`:
   ```python
   Add_Employee(host, user, password, database, name, height, weight)
   ```

### 4. **Check Staff**
   Retrieve and display all employee data using `Check_Staff()`:
   ```python
   Check_Staff(host, user, password, database)
   ```

## Example Usage

```python
# Connecting to the MySQL server and creating a database
host = "localhost"
user = "root"
password = "yourpassword"
database = "staff_db"

Create_Database(host, user, password, database)

# Create a table for employees
Create_Table(host, user, password, database)

# Adding employees to the table
Add_Employee(host, user, password, database, "John Doe", 180, 75)
Add_Employee(host, user, password, database, "Jane Smith", 165, 60)

# Displaying the list of employees
Check_Staff(host, user, password, database)
```

## Contribution

Feel free to fork the repository and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.