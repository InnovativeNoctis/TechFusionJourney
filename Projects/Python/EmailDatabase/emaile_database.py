import re
import bcrypt  # Library for hashing passwords
import mysql.connector  # MySQL database connector

def Create_Database(host, user, password, database):
    """
    Creates a MySQL database if it doesn't already exist.
    
    Parameters:
        host (str): MySQL server address
        user (str): MySQL username
        password (str): MySQL password
        database (str): Name of the database to be created
    """
    print("--> Connecting...")
    try:
        with mysql.connector.connect(host=host, user=user, password=password) as connect:
            if connect.is_connected():
                print("Connected to MySQL!")
                
                cursor = connect.cursor()
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
                print("--> Database created successfully!")
                print(f"--> Database name: {database}")
                
                cursor.close()
            else:
                print("--> Error: Connection failed!")
    except mysql.connector.Error as err:
        print(f"--> Error: {err}")

def Create_Table(host, user, password, database):
    """
    Creates the 'email_list' table if it doesn't already exist.
    The table contains two columns: email and password.
    
    Parameters:
        host (str): MySQL server address
        user (str): MySQL username
        password (str): MySQL password
        database (str): Name of the database to use
    """
    print("--> Connecting...")
    try:
        with mysql.connector.connect(host=host, user=user, password=password, database=database) as connect:
            if connect.is_connected():
                print("--> Connected to MySQL database!")
                print(f"--> Database: {database}")  
                
                cursor = connect.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS email_list (
                        email VARCHAR(100) NOT NULL PRIMARY KEY,
                        password VARCHAR(255) NOT NULL
                    )
                """)
                print("\n--> Table created successfully!")
                print("--> Table: email_list")
                
                print("\nDescribe Table:")
                cursor.execute("DESCRIBE email_list")
                for row in cursor:
                    print(row)
                
                cursor.close()  
    except mysql.connector.Error as err:
        print(f"--> Error: {err}")

def Add_Email(host, user, password, database, email, epassword):
    """
    Inserts a new email and its hashed password into the 'email_list' table.
    
    Parameters:
        host (str): MySQL server address
        user (str): MySQL username
        password (str): MySQL password
        database (str): Name of the database to use
        email (str): Email address to store
        epassword (str): Plain-text password (which will be hashed)
    """
    print("--> Connecting... ")
    try:
        with mysql.connector.connect(host=host, user=user, password=password, database=database) as connect:
            if connect.is_connected():
                print("--> Connected to MySQL database!")
                print(f"--> Database: {database}")  

                cursor = connect.cursor()
                
                # Hash the password before storing
                hashed_password = bcrypt.hashpw(epassword.encode(), bcrypt.gensalt())

                # Insert email and hashed password into the table
                cursor.execute("INSERT INTO email_list (email, password) VALUES (%s, %s)", (email, hashed_password.decode()))
                connect.commit()  
                print(f"\n--> {cursor.rowcount} record inserted!")  

                print("\n--> Updated table:")
                cursor.execute("SELECT * FROM email_list")
                for row in cursor:
                    print(row)
                
                cursor.close() 
    except mysql.connector.Error as err:
        print(f"--> Error: {err}")

def Check_Email(host, user, password, database):
    """
    Retrieves and displays all stored emails from the 'email_list' table.
    Passwords are not displayed for security reasons.
    
    Parameters:
        host (str): MySQL server address
        user (str): MySQL username
        password (str): MySQL password
        database (str): Name of the database to use
    """
    print("--> Connecting... ")
    try:
        with mysql.connector.connect(host=host, user=user, password=password, database=database) as connect:
            if connect.is_connected():
                print("--> Connected to MySQL database!")
                print(f"--> Database: {database}")  

                cursor = connect.cursor()
                print("\n--> Email List:")
                cursor.execute("SELECT email FROM email_list")  # Only show emails, not passwords
                for row in cursor:
                    print(row[0])
                
                cursor.close()  
    except mysql.connector.Error as err:
        print(f"--> Error: {err}")

def main():
    """
    The main function that runs the program.
    - Asks for MySQL connection details
    - Creates the database and table if they do not exist
    - Allows the user to input email addresses and store them securely
    - Finally, displays all stored emails
    """
    host = input("Enter MySQL host (e.g., localhost): ")
    user = input("Enter MySQL username: ")
    password = input("Enter MySQL password: ")
    database = input("Enter name for the (new) database: ")

    print("\n")
    Create_Database(host, user, password, database)

    print("\n")
    Create_Table(host, user, password, database)
    print("\n")
    
    while True:
        print("\nEnter the information below:")
        email = input("Enter email: ")
        
        # Validate email format using regex
        valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
        
        if valid:
            epassword = input("Enter email password: ")
            Add_Email(host, user, password, database, email, epassword)

            more = input("\nDo you want to add another email? (yes/no): ")
            if more.lower() != "yes":
                break
        else:
            print("Error: Invalid Email Address!")

    Check_Email(host, user, password, database)

if __name__ == "__main__":
    main()