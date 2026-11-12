# MODULE 4 - LAB 3: CSV-Based Payroll Management System
# Calculates employee salary and stores payroll records in a CSV file.

import csv
from pathlib import Path

PAYROLL_FILE = Path("payroll.csv")

FIELDNAMES = [
    "Employee ID", "Name", "Basic Salary",
    "HRA", "DA", "Deduction", "Gross Salary", "Net Salary"
]

def create_payroll_file():
    if not PAYROLL_FILE.exists():
        with PAYROLL_FILE.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()

def add_employee():
    employee_id = input("Enter employee ID: ").strip()
    name = input("Enter employee name: ").strip()

    try:
        basic = float(input("Enter basic salary: "))
        hra_percent = float(input("Enter HRA percentage: "))
        da_percent = float(input("Enter DA percentage: "))
        deduction = float(input("Enter total deduction: "))

        if min(basic, hra_percent, da_percent, deduction) < 0:
            print("Salary values and percentages cannot be negative.")
            return
    except ValueError:
        print("Please enter valid numeric salary values.")
        return

    create_payroll_file()

    with PAYROLL_FILE.open("r", newline="", encoding="utf-8") as file:
        existing_records = list(csv.DictReader(file))

    if any(row["Employee ID"] == employee_id for row in existing_records):
        print("Employee ID already exists.")
        return

    hra = basic * hra_percent / 100
    da = basic * da_percent / 100
    gross = basic + hra + da
    net = gross - deduction

    record = {
        "Employee ID": employee_id,
        "Name": name,
        "Basic Salary": f"{basic:.2f}",
        "HRA": f"{hra:.2f}",
        "DA": f"{da:.2f}",
        "Deduction": f"{deduction:.2f}",
        "Gross Salary": f"{gross:.2f}",
        "Net Salary": f"{net:.2f}",
    }

    with PAYROLL_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow(record)

    print("\nPayroll record saved successfully.")
    print(f"Gross Salary: Rs. {gross:,.2f}")
    print(f"Net Salary:   Rs. {net:,.2f}")

def view_payroll():
    create_payroll_file()

    with PAYROLL_FILE.open("r", newline="", encoding="utf-8") as file:
        records = list(csv.DictReader(file))

    if not records:
        print("No payroll records found.")
        return

    print("\n===== PAYROLL REPORT =====")
    for row in records:
        print(
            f"{row['Employee ID']} | {row['Name']} | "
            f"Gross: Rs. {row['Gross Salary']} | "
            f"Net: Rs. {row['Net Salary']}"
        )

def main():
    while True:
        print("\n===== CSV PAYROLL MANAGEMENT =====")
        print("1. Add Employee Payroll")
        print("2. View Payroll Report")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_payroll()
        elif choice == "3":
            print("Exiting Payroll Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
