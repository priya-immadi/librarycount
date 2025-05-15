import json
import os

FILENAME = 'library.json'

# Load book data from file
def load_library():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            return json.load(file)
    return {}

# Save book data to file
def save_library(library):
    with open(FILENAME, 'w') as file:
        json.dump(library, file, indent=4)

# Add a new book
def add_book(library):
    title = input("Enter book title: ").strip()
    author = input("Enter author: ").strip()
    if title in library:
        print("Book already exists.")
    else:
        library[title] = {'author': author, 'available': True}
        print(f"'{title}' added to the library.")

# View all books
def view_books(library):
    if not library:
        print("Library is empty.")
    else:
        print("\n--- Library Books ---")
        for title, info in library.items():
            status = "Available" if info['available'] else "Borrowed"
            print(f"Title: {title}, Author: {info['author']}, Status: {status}")

# Borrow a book
def borrow_book(library):
    title = input("Enter the title of the book to borrow: ").strip()
    if title in library:
        if library[title]['available']:
            library[title]['available'] = False
            print(f"You have borrowed '{title}'.")
        else:
            print(f"'{title}' is already borrowed.")
    else:
        print("Book not found.")

# Return a book
def return_book(library):
    title = input("Enter the title of the book to return: ").strip()
    if title in library:
        if not library[title]['available']:
            library[title]['available'] = True
            print(f"You have returned '{title}'.")
        else:
            print(f"'{title}' was not borrowed.")
    else:
        print("Book not found.")

# Delete a book
def delete_book(library):
    title = input("Enter the title of the book to delete: ").strip()
    if title in library:
        del library[title]
        print(f"'{title}' has been deleted.")
    else:
        print("Book not found.")

# Main menu loop
def main():
    library = load_library()
    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Delete Book")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_book(library)
        elif choice == '2':
            view_books(library)
        elif choice == '3':
            borrow_book(library)
        elif choice == '4':
            return_book(library)
        elif choice == '5':
            delete_book(library)
        elif choice == '6':
            save_library(library)
            print("Library saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
