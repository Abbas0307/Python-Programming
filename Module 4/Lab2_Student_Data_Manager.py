# MODULE 4 - LAB 2: Student Data Manager using Files
# Adds, displays, and searches student records stored in a text file.

from pathlib import Path

DATA_FILE = Path("students.txt")

def add_student():
    roll_no = input("Enter roll number: ").strip()
    name = input("Enter student name: ").strip()
    department = input("Enter department: ").strip()

    if not roll_no or not name or not department:
        print("All fields are required.")
        return

    # Prevent duplicate roll numbers.
    if DATA_FILE.exists():
        for line in DATA_FILE.read_text(encoding="utf-8").splitlines():
            if line.split("|")[0] == roll_no:
                print("A student with this roll number already exists.")
                return

    with DATA_FILE.open("a", encoding="utf-8") as file:
        file.write(f"{roll_no}|{name}|{department}\n")

    print("Student record saved successfully.")

def view_students():
    if not DATA_FILE.exists() or not DATA_FILE.read_text(encoding="utf-8").strip():
        print("No student records found.")
        return

    print("\n===== STUDENT RECORDS =====")
    print(f"{'Roll No':<12}{'Name':<22}{'Department'}")
    print("-" * 48)

    with DATA_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split("|")
            if len(parts) == 3:
                roll_no, name, department = parts
                print(f"{roll_no:<12}{name:<22}{department}")

def search_student():
    search_roll = input("Enter roll number to search: ").strip()

    if not DATA_FILE.exists():
        print("No student records found.")
        return

    with DATA_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split("|")
            if len(parts) == 3 and parts[0] == search_roll:
                print("\nStudent found:")
                print("Roll Number:", parts[0])
                print("Name:", parts[1])
                print("Department:", parts[2])
                return

    print("Student not found.")

def main():
    while True:
        print("\n===== STUDENT DATA MANAGER =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting Student Data Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
