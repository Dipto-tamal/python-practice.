# Student Result Management System

students = []

def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students.append([name, marks])
    print("Student added successfully!\n")

def show_students():
    print("\n--- Student List ---")
    for s in students:
        print("Name:", s[0], "Marks:", s[1])
    print()

def calculate_grade(marks):
    if marks >= 80:
        return "A+"
    elif marks >= 70:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

def show_result():
    print("\n--- Student Results ---")
    for s in students:
        grade = calculate_grade(s[1])
        print(s[0], "→", s[1], "→ Grade:", grade)
    print()

while True:
    print("1. Add Student")
    print("2. Show Students")
    print("3. Show Result")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        show_result()
    elif choice == "4":
        print("Goodbye Dipto 👋")
        break
    else:
        print("Invalid choice!\n")
1