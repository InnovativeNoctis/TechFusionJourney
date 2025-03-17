import mysql.connector

# Function to create a new database
def Create_Database(host, user, password, database):
    print("--> Connecting...")
    try:
        # Connect to MySQL server without specifying a database
        connect = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        if connect.is_connected():
            print("--> Connected to MySQL!")

            # Create a cursor object to execute SQL queries
            cursor = connect.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")  # SQL to create a database
            print("--> Database created successfully!")
            print(f"--> Database name: {database}")

            cursor.close()  # Close the cursor after executing the query
        else:
            print("--> Error: Connection failed!")

    except mysql.connector.Error as err:
        # Handle any errors that occur during the connection or execution
        print(f"--> Error: {err}")

    finally:
        # Ensure that the connection is closed when done
        if 'connect' in locals() and connect.is_connected():
            connect.close()
            print("--> Connection closed.")

# Function to create a new table in the database
def Create_Table(host, user, password, database):
    print("--> Connecting...")
    try:
        # Connect to the MySQL server with the specified database
        connect = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connect.is_connected():
            print("--> Connected to MySQL database!")
            print(f"--> Database: {database}")  
            
            # Create a cursor object to execute SQL queries
            cursor = connect.cursor()
            # SQL query to create the 'people' table if it doesn't already exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS people (
                    name VARCHAR(100) NOT NULL,
                    weight FLOAT CHECK (weight > 0),
                    height FLOAT CHECK (height > 0)
                )
            """)
            print("\n--> Table created successfully!")
            print("--> Table: people")
            
            # Describe the 'people' table to display the structure
            print("\nDescribe:")
            cursor.execute("DESCRIBE people")
            for row in cursor:
                print(row)
            
            cursor.close()  # Close the cursor after executing the query
            
        else:
            print("--> Connection failed!")

    except mysql.connector.Error as err:
        # Handle any errors that occur during the connection or execution
        print(f"--> Error: {err}")
    
    finally:
        # Ensure that the connection is closed when done
        if 'connect' in locals() and connect.is_connected():
            connect.close()
            print("--> Connection closed.")

# Function to add a new employee to the 'people' table
def Add_Employee(host, user, password, database, name, height, weight):
    print("--> Connecting... ")
    try:
        # Connect to the MySQL server with the specified database
        connect = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connect.is_connected():
            print("--> Connected to MySQL database!")
            print(f"--> Database: {database}")  

            # Create a cursor object to execute SQL queries
            cursor = connect.cursor()
            # SQL query to insert employee data into the 'people' table
            cursor.execute("INSERT INTO people (name, weight, height) VALUES (%s, %s, %s)", (name, weight, height))
            connect.commit()  # Commit the transaction to save changes
            print(f"\n--> {cursor.rowcount} record inserted!")  # Show the number of records inserted

            # Display all records in the 'people' table after insertion
            print("\n--> Updated table:")
            cursor.execute("SELECT * FROM people")
            for row in cursor:
                print(row)
            
            cursor.close()  # Close the cursor after executing the query
            
        else:
            print("--> Connection failed!")

    except mysql.connector.Error as err:
        # Handle any errors that occur during the connection or execution
        print(f"--> Error: {err}")
    
    finally:
        # Ensure that the connection is closed when done
        if 'connect' in locals() and connect.is_connected():
            connect.close()
            print("--> Connection closed.")

# Function to check and display all staff records from the 'people' table
def Check_Staff(host, user, password, database):
    print("--> Connecting... ")
    try:
        # Connect to the MySQL server with the specified database
        connect = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connect.is_connected():
            print("--> Connected to MySQL database!")
            print(f"--> Database: {database}")  

            # Create a cursor object to execute SQL queries
            cursor = connect.cursor()
            print("\n--> Staff:")
            # SQL query to retrieve all records from the 'people' table
            cursor.execute("SELECT * FROM people")
            for row in cursor:
                print(row)
            
            cursor.close()  # Close the cursor after executing the query
            
        else:
            print("--> Connection failed!")

    except mysql.connector.Error as err:
        # Handle any errors that occur during the connection or execution
        print(f"--> Error: {err}")
    
    finally:
        # Ensure that the connection is closed when done
        if 'connect' in locals() and connect.is_connected():
            connect.close()
            print("--> Connection closed.")


# Main code to take user input for the database operations
def main():
    # Prompt user for MySQL connection details
    host = input("Enter MySQL host (e.g., localhost): ")
    user = input("Enter MySQL username: ")
    password = input("Enter MySQL password: ")
    database = input("Enter name for the new database: ")

    # Create Database
    Create_Database(host, user, password, database)

    # Create Table in the database
    Create_Table(host, user, password, database)

    # Add Employees to the 'people' table
    while True:
        print("\nEnter employee details to add:")
        name = input("Enter employee name: ")
        height = float(input("Enter employee height (in cm): "))
        weight = float(input("Enter employee weight (in kg): "))
        
        # Add employee record
        Add_Employee(host, user, password, database, name, height, weight)

        # Ask user if they want to add another employee
        more = input("\nDo you want to add another employee? (yes/no): ")
        if more.lower() != "yes":
            break

    # Display all staff records in the 'people' table
    Check_Staff(host, user, password, database)


if __name__ == "__main__":
    # Run the main function when the script is executed
    main()