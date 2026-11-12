# MODULE 4 - LAB 4: CSV-Based Payroll Management System
# Accepts employee details, calculates net salary, and stores records in payroll.csv.

import csv

try:
    n = int(input("Enter number of employees: "))

    if n <= 0:
        print("Please enter at least one employee.")
    else:
        with open("payroll.csv", "w", newline="", encoding="utf-8") as file:
            fieldnames = [
                "Employee ID",
                "Name",
                "Basic Salary",
                "Allowance",
                "Deduction",
                "Net Salary"
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for i in range(n):
                print(f"\nEnter details for employee {i + 1}:")
                employee_id = input("Enter Employee ID: ").strip()
                name = input("Enter Name: ").strip()

                try:
                    basic_salary = float(input("Enter Basic Salary: "))
                    allowance = float(input("Enter Allowance: "))
                    deduction = float(input("Enter Deduction: "))

                    if min(basic_salary, allowance, deduction) < 0:
                        print("Salary values cannot be negative. Employee skipped.")
                        continue

                    net_salary = basic_salary + allowance - deduction

                    writer.writerow({
                        "Employee ID": employee_id,
                        "Name": name,
                        "Basic Salary": f"{basic_salary:.2f}",
                        "Allowance": f"{allowance:.2f}",
                        "Deduction": f"{deduction:.2f}",
                        "Net Salary": f"{net_salary:.2f}"
                    })

                    print(f"Net Salary: Rs. {net_salary:.2f}")

                except ValueError:
                    print("Invalid salary input. Employee skipped.")

        print("\nEmployee payroll records saved in payroll.csv.")

        print("\n===== EMPLOYEE PAYROLL RECORDS =====")
        with open("payroll.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(
                    f"{row['Employee ID']} | {row['Name']} | "
                    f"Basic Salary: Rs. {row['Basic Salary']} | "
                    f"Allowance: Rs. {row['Allowance']} | "
                    f"Deduction: Rs. {row['Deduction']} | "
                    f"Net Salary: Rs. {row['Net Salary']}"
                )

except ValueError:
    print("Please enter a valid number of employees.")
