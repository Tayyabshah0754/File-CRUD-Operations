from pathlib import Path

def main_menu():
    while True:
        print("\n===== MAIN MENU =====")
        print("Want to Signup            Press 1")
        print("Want to Login              Press 2")
        print("Want to login as ( Admin ) Press 3")
        print("Want to Exit               Press 0")
        try:
            choice = int(input("Enter your Choice :- "))
        except ValueError:
            print("Invalid input ")
            continue

        if choice == 1:
            signup()
        elif choice == 2:
            login()
        elif choice == 3:
            admin_login()
        elif choice == 0:
            print("Exiting Program ")
            break
        else:
            print("Invalid input ")


# ---------------- FILE CRUD ----------------

def write_in_file():
    filename = input("Enter the name of file :- ")
    path = Path(filename)
    if not path.exists():
        with open(path, 'w') as f:
            data = input("Enter what you want to write in file :- ")
            f.write(data)
        print("File written successfully ")
    else:
        print("File Named", filename, "Already exists ")


def read_from_file():
    filename = input("Enter the name of file :- ")
    path = Path(filename)
    if path.exists():
        with open(path, 'r') as f:
            data = f.read()
        print("-----------------File Content-----------------")
        print(data)
    else:
        print("File Named", filename, "Not exists ")


def update_from_file():
    filename = input("Enter the name of file :- ")
    path = Path(filename)
    if path.exists():
        print("Want to rename file                 Press 1 ")
        print("want to append data in file         Press 2 ")
        print("Want to overwrite data in the file  Press 3 ")
        try:
            option = int(input("Enter your Choice :- "))
        except ValueError:
            print("Invalid Option")
            return

        if option == 1:
            newname = input("Enter the new name of the file :- ")
            newpath = Path(newname)
            if newpath.exists():
                print("Name already Exists ")
            else:
                path.rename(newname)
                print("File renamed successfully")
        elif option == 2:
            with open(path, 'a') as ff:
                data = input("Enter what you want to append in a file :- ")
                ff.write(data)
            print("Data Appended successfully ")
        elif option == 3:
            with open(path, 'w') as ff:
                data = input("Enter what you want to overwrite in a file :- ")
                ff.write(data)
            print("Data Overwrite successfully ")
        else:
            print("Invalid Option")
    else:
        print("File Not Found")


def delete_from_file():
    name = input("Enter the name of file you want to delete :- ")
    path = Path(name)
    if path.exists():
        path.unlink()
        print("File deleted successfully ")
    else:
        print("File not found")


def user_menu():
    while True:
        print("\n----- USER MENU -----")
        print("Want to ( Write  ) in a file   Press 1")
        print("Want to ( Read   ) from a file Press 2")
        print("Want to ( Update ) in a file   Press 3")
        print("Want to ( Delete ) in a file   Press 4")
        print("Want to ( Exit   )             Press 0")
        try:
            user_menu_choice = int(input("Enter your choice :- "))
        except ValueError:
            print("Invalid input ")
            continue

        if user_menu_choice == 1:
            write_in_file()
        elif user_menu_choice == 2:
            read_from_file()
        elif user_menu_choice == 3:
            update_from_file()
        elif user_menu_choice == 4:
            delete_from_file()
        elif user_menu_choice == 0:
            break
        else:
            print("Invalid input ")


# ---------------- SIGNUP / LOGIN ----------------

def load_accounts():
    """Returns a dict of {email: password} read from the file."""
    try:
        with open("Login_details.txt", 'r') as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        lines = []

    accounts = {}
    for line in lines:
        parts = line.split(',')
        if len(parts) == 2:
            accounts[parts[0]] = parts[1]
    return accounts


def signup():
    email = input("Enter your Email :- ")
    password = input("Enter your Password :- ")

    accounts = load_accounts()

    if email in accounts:
        print("\nEmail already exists. Signup Failed.... ")
        return

    with open("Login_details.txt", 'a') as ff:
        ff.write(email + "," + password + "\n")

    print("\nSignup Successful ")


def login():
    email = input("Enter your Email :- ")
    password = input("Enter your Password :- ")

    accounts = load_accounts()

    if email not in accounts:
        print("\nNo account found with this email. Please sign up first.")
        return

    if accounts[email] != password:
        print("\nIncorrect password. Login Failed.")
        return

    print("\nLogin Successful ")
    user_menu()


# ---------------- ADMIN ----------------

def show_all_logins():
    accounts = load_accounts()
    if not accounts:
        print("Empty Record ")
        return
    print("-----------------Registered Emails-----------------")
    for email in accounts:
        print(email)


def admin_menu():
    while True:
        print("\n----- ADMIN MENU -----")
        print("Want to see all the logins  Press 1")
        print("Want to Exit to main menu   Press 0")
        try:
            admin_menu_choice = int(input("Enter your choice :- "))
        except ValueError:
            print("Invalid input ")
            continue

        if admin_menu_choice == 1:
            show_all_logins()
        elif admin_menu_choice == 0:
            break
        else:
            print("Invalid Input ")


def admin_login():
    correct_password = "unknown"
    entered_password = input("Enter admin password :- ")
    if entered_password == correct_password:
        print("Logged in Successfully ")
        admin_menu()
    else:
        print("\nInvalid password")


# ---------------- START ----------------

print("Welcome to file CRUD operations program")
main_menu()