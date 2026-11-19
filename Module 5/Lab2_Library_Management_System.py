# MODULE 5 - LAB 2: Library Management System
# Book records are stored in a text file.

from pathlib import Path

BOOK_FILE = Path("library_books.txt")


def add_book():
    book_id = input("Enter book ID: ").strip()
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()

    if not book_id or not title or not author:
        print("All fields are required.")
        return

    if BOOK_FILE.exists():
        for line in BOOK_FILE.read_text(encoding="utf-8").splitlines():
            if line.split("|")[0] == book_id:
                print("A book with this ID already exists.")
                return

    with BOOK_FILE.open("a", encoding="utf-8") as file:
        file.write(f"{book_id}|{title}|{author}\n")
    print("Book added successfully.")


def view_books():
    if not BOOK_FILE.exists() or not BOOK_FILE.read_text(encoding="utf-8").strip():
        print("No books found in the library.")
        return

    print("\n===== LIBRARY BOOKS =====")
    print(f"{'Book ID':<12}{'Title':<25}{'Author'}")
    print("-" * 55)

    with BOOK_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split("|")
            if len(parts) == 3:
                print(f"{parts[0]:<12}{parts[1]:<25}{parts[2]}")


def search_book():
    search_id = input("Enter book ID to search: ").strip()

    if BOOK_FILE.exists():
        with BOOK_FILE.open("r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 3 and parts[0] == search_id:
                    print("\nBook found:")
                    print("Book ID:", parts[0])
                    print("Title:", parts[1])
                    print("Author:", parts[2])
                    return

    print("Book not found.")


def main():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            print("Exiting Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
