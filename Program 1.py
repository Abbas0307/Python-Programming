# Student Details Program

# Accept inputs
name = input("Enter Student Name: ")
usn = input("Enter USN: ")
branch = input("Enter Branch: ")
semester = input("Enter Semester: ")

mark1 = float(input("Enter Marks of Subject 1: "))
mark2 = float(input("Enter Marks of Subject 2: "))
mark3 = float(input("Enter Marks of Subject 3: "))

# Calculate total and average
total = mark1 + mark2 + mark3
average = total / 3

# Display formatted output
print("\n========== STUDENT DETAILS ==========")
print(f"Student Name : {name}")
print(f"USN          : {usn}")
print(f"Branch       : {branch}")
print(f"Semester     : {semester}")
print(f"Subject 1    : {mark1}")
print(f"Subject 2    : {mark2}")
print(f"Subject 3    : {mark3}")
print("-------------------------------------")
print(f"Total Marks  : {total}")
print(f"Average Marks: {average:.2f}")
print("=====================================")
