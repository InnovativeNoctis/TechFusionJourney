# 📧 Email Database Management

This project provides a **MySQL-based email storage system** with **secure password hashing**. It allows users to:
- Create a MySQL database and table for storing emails.
- Insert emails and securely hash passwords before storing them.
- Validate email format using regex.
- Display stored email addresses (passwords are not shown for security).

---

## 🛠️ Requirements

Make sure you have the following installed:
- **Python 3.x**
- **MySQL Server**
- Required Python libraries:
  ```bash
  pip install mysql-connector-python bcrypt
  ```

---

## 🚀 How to Use

1️⃣ **Run the script**:
   ```bash
   python email_database.py
   ```

2️⃣ **Enter your MySQL connection details** when prompted.

3️⃣ **Add email addresses** and corresponding passwords (which will be securely hashed).

4️⃣ **View stored emails** (passwords are hidden for security).

---

## 🔐 Security Features

- **Passwords are hashed using `bcrypt`** before storage, preventing plain-text password leaks.
- **Database connection is managed securely** to prevent SQL injection vulnerabilities.
- **Validates email format** to ensure only properly formatted addresses are stored.

---

## 📂 Project Structure

```
EmailDatabase/
│── email_database.py    # Main script
│── README.md            # Project documentation
```

---

## 📜 License

This project is open-source. Feel free to modify and use it as needed.

---

## 📩 Contact

If you have any questions or improvements, feel free to contribute or reach out!

GitHub: [@InnovativeNoctis](https://github.com/InnovativeNoctis)