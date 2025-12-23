
import os

FILENAME = "students.txt"

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    with open(FILENAME, "a") as file:
        file.write(f"{roll},{name},{course},{marks}\n")

    print("Student added successfully!\n")


def view_students():
    if not os.path.exists(FILENAME):
        print("No records found.\n")
        return

    with open(FILENAME, "r") as file:
        students = file.readlines()

    if not students:
        print("No records available.\n")
        return

    print("\nRoll | Name | Course | Marks")
    print("-" * 30)
    for student in students:
        roll, name, course, marks = student.strip().split(",")
        print(f"{roll} | {name} | {course} | {marks}")
    print()


def search_student():
    roll_no = input("Enter roll number to search: ")

    with open(FILENAME, "r") as file:
        for student in file:
            roll, name, course, marks = student.strip().split(",")
            if roll == roll_no:
                print("\nStudent Found:")
                print(f"Roll: {roll}")
                print(f"Name: {name}")
                print(f"Course: {course}")
                print(f"Marks: {marks}\n")
                return

    print("Student not found.\n")


def delete_student():
    roll_no = input("Enter roll number to delete: ")
    found = False

    with open(FILENAME, "r") as file:
        students = file.readlines()

    with open(FILENAME, "w") as file:
        for student in students:
            roll, name, course, marks = student.strip().split(",")
            if roll != roll_no:
                file.write(student)
            else:
                found = True

    if found:
        print("Student record deleted.\n")
    else:
        print("Student not found.\n")


def main():
    while True:
        print("----- Student Management System -----")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")


main()

