# File-CRUD-Operations
Python-based file CRUD operations system with signup, login, and admin functionality.
# File CRUD Operations System

A Python-based file management system that allows users to perform CRUD (Create, Read, Update, Delete) operations on files. The project also includes a signup/login system and a separate admin panel.

## 📌 Project Overview

This project is a console-based Python application designed to demonstrate:

- File handling in Python
- CRUD operations
- User signup and login
- Admin authentication
- Menu-driven programming
- Exception handling
- Working with the `pathlib` module

## ✨ Features

### 👤 User Features

Users can:

- Sign up with an email and password
- Log in to their account
- Create/write data to a file
- Read file contents
- Update existing files
- Rename files
- Append data to files
- Overwrite file contents
- Delete files
- Return to the main menu

### 🔐 Admin Features

The admin can:

- Log in using an admin password
- View all registered email addresses
- Return to the main menu

## 🛠️ Technologies Used

- Python
- File Handling
- `pathlib`
- Exception Handling
- Dictionaries
- Functions
- Loops
- Conditional Statements

## 📂 Project Structure

```text
File-CRUD-Operations/
│
├── main.py
└── README.md
▶️ How to Run
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL
2. Open the project folder
cd File-CRUD-Operations
3. Run the program
python main.py
🖥️ Main Menu
===== MAIN MENU =====
Want to Signup            Press 1
Want to Login             Press 2
Want to login as ( Admin ) Press 3
Want to Exit              Press 0
📁 File Operations

After successfully logging in, the user can access:

----- USER MENU -----
Want to ( Write  ) in a file   Press 1
Want to ( Read   ) from a file Press 2
Want to ( Update ) in a file   Press 3
Want to ( Delete ) in a file   Press 4
Want to ( Exit   )             Press 0
📚 Concepts Demonstrated

This project demonstrates practical use of Python concepts such as:

Functions
while loops
if-elif-else
try-except
File modes (r, w, a)
Path.exists()
Path.rename()
Path.unlink()
Dictionaries
User authentication
Modular program design
⚠️ Security Note

This project is created for educational purposes. Passwords are stored in a local text file and should not be used for real-world authentication systems.

For a production application, passwords should be securely hashed and sensitive credentials should not be hard-coded in the source code.

🚀 Future Improvements

Possible improvements include:

Password hashing
Better input validation
Separate user data files
File search functionality
Better error handling
Graphical user interface
Database integration
Role-based access control
👨‍💻 Author

Tayyab Shah

Computer Science Student
Python | Machine Learning | AI