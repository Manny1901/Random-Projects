import json
from datetime import datetime, timedelta

# Initialize JSON file paths
LIBRARY_DATA_FILE = "library_data.json"
USERS_DATA_FILE = "users_data.json"

# Pre-defined librarian account
LIBRARIAN_CREDENTIALS = {"username": "librarian", "password": "admin123"}

# Initialize the library with some sample books
library = {
    "books": {
        "Python Programming": 15,
        "Data Science Essentials": 15,
        "Artificial Intelligence": 15,
        "Machine Learning": 15,
        "Deep Learning": 15,
    },
    "borrowed_books": {}
}

# Functions to load and save data persistently
def load_data(file_path, default_data):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return default_data

def save_data(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

# Load data
library = load_data(LIBRARY_DATA_FILE, library)
users = load_data(USERS_DATA_FILE, {})

# Librarian functionalities
def librarian_menu():
    print("\nLibrarian Menu:")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. Count Books")
    print("4. Delete a User Account")
    print("5. View Borrowed Books")
    print("6. Log Out")
    choice = input("Enter your choice: ")
    return choice

def add_book():
    book_name = input("Enter the name of the book to add: ")
    if book_name in library["books"]:
        library["books"][book_name] += 10
        print(f"{book_name} stock replenished to {library['books'][book_name]} copies.")
    else:
        library["books"][book_name] = 10
        print(f"{book_name} added with 10 copies.")

def remove_book():
    book_name = input("Enter the name of the book to remove: ")
    if book_name in library["books"]:
        del library["books"][book_name]
        print(f"{book_name} removed from the library.")
    else:
        print(f"{book_name} does not exist in the library.")

def count_books():
    print("\nBooks in Library:")
    for book, stock in library["books"].items():
        print(f"{book}: {stock} copies")

def delete_user():
    username = input("Enter the username to delete: ")
    if username in users and username != LIBRARIAN_CREDENTIALS["username"]:
        del users[username]
        print(f"User {username} deleted.")
    else:
        print(f"Cannot delete user {username} (does not exist or is the librarian).")

def view_borrowed_books():
    print("\nBorrowed Books:")
    for user, borrowed in library["borrowed_books"].items():
        print(f"{user}: {borrowed}")

# User functionalities
def user_menu():
    print("\nUser Menu:")
    print("1. Borrow a Book")
    print("2. Delete My Account")
    print("3. Log Out")
    choice = input("Enter your choice: ")
    return choice

def borrow_book(username):
    print("\nAvailable Books to Borrow:")
    for book, stock in library["books"].items():
        if stock > 0:
            print(f"{book}: {stock} copies")
    book_name = input("\nEnter the name of the book to borrow: ")
    if book_name in library["books"] and library["books"][book_name] > 0:
        library["books"][book_name] -= 1
        borrowed_date = datetime.now()
        due_date = borrowed_date + timedelta(weeks=1)
        library["borrowed_books"].setdefault(username, []).append({
            "book": book_name,
            "borrowed_date": borrowed_date.strftime("%Y-%m-%d %H:%M:%S"),
            "due_date": due_date.strftime("%Y-%m-%d %H:%M:%S"),
        })
        print(f"You have borrowed {book_name}. It is due by {due_date.strftime('%Y-%m-%d %H:%M:%S')}.")
    else:
        print(f"{book_name} is out of stock. It will be replenished in a week.")

def delete_account(username):
    confirm = input("Are you sure you want to delete your account? (yes/no): ").strip().lower()
    if confirm == "yes":
        del users[username]
        library["borrowed_books"].pop(username, None)
        print("Your account has been deleted.")
        return True
    return False

# Login and account creation
def login():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    if username == LIBRARIAN_CREDENTIALS["username"] and password == LIBRARIAN_CREDENTIALS["password"]:
        print("Logged in as Librarian.")
        return "librarian"
    elif username in users and users[username]["password"] == password:
        print(f"Welcome back, {username}!")
        return username
    else:
        print("Invalid credentials.")
        return None

def create_account():
    username = input("Enter a username: ").strip()
    if username in users or username == LIBRARIAN_CREDENTIALS["username"]:
        print("Username already exists. Choose a different username.")
        return
    password = input("Enter a password: ").strip()
    users[username] = {"password": password}
    print(f"Account created successfully! Welcome, {username}!")

# Main program
def main():
    while True:
        print("\nWelcome to the Library Management System!")
        print("1. Log In")
        print("2. Create an Account")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            user = login()
            if user == "librarian":
                while True:
                    choice = librarian_menu()
                    if choice == "1":
                        add_book()
                    elif choice == "2":
                        remove_book()
                    elif choice == "3":
                        count_books()
                    elif choice == "4":
                        delete_user()
                    elif choice == "5":
                        view_borrowed_books()
                    elif choice == "6":
                        break
                    else:
                        print("Invalid choice.")
            elif user:
                while True:
                    choice = user_menu()
                    if choice == "1":
                        borrow_book(user)
                    elif choice == "2":
                        if delete_account(user):
                            break
                    elif choice == "3":
                        break
                    else:
                        print("Invalid choice.")
        elif choice == "2":
            create_account()
        elif choice == "3":
            save_data(LIBRARY_DATA_FILE, library)
            save_data(USERS_DATA_FILE, users)
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
