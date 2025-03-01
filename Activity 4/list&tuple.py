import os

students = []

def save_file(filename="Activity 4/students.txt"):
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)
    try:
        with open(filename, "w") as file:
            for s in students:
                file.write(f"{s[0]}|{s[1][0]}|{s[1][1]}|{s[2]}|{s[3]}\n")
        print(f"Records saved successfully.")
    except Exception as e:
        print(f"Error saving file: {e}")

def save_as_file():
    save_file()
    print("File saved as 'students.txt'")

def open_file(filename="Activity 4/students.txt"):
    global students
    if not os.path.exists(filename):
        print("No previous records found.")
        return
    try:
        with open(filename, "r") as file:
            students.clear()
            for line in file:
                parts = line.strip().split("|")
                students.append((parts[0], (parts[1], parts[2]), float(parts[3]), float(parts[4])))
        print("Records loaded successfully.")
    except Exception as e:
        print(f"Error loading file: {e}")

def show_all_students():
    if not students:
        print("No student records available.")
        return
    print("\nShow All Students Record:")
    choice = input("Choose an option (1. Last Name, 2. Grade): ")
    sorted_students = students[:]
    for s in sorted_students:
        final_grade = 0.6 * s[2] + 0.4 * s[3]
        print(f"ID: {s[0]}, Name: {s[1][0]} {s[1][1]}, Class Standing: {s[2]}, Major Exam: {s[3]}, Final Grade: {final_grade:.2f}")

def add_record():
    student_id = input("Enter a 6-digit Student ID: ")
    if not student_id.isdigit() or len(student_id) != 6:
        print("Invalid ID. Must be a 6-digit number.")
        return
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    try:
        class_standing = float(input("Enter Class Standing Grade: "))
        major_exam = float(input("Enter Major Exam Grade: "))
    except ValueError:
        print("Grades must be numeric.")
        return
    students.append((student_id, (first_name, last_name), class_standing, major_exam))
    print("Student record added.")

def show_student():
    student_id = input("Enter Student ID to search: ")
    for s in students:
        if s[0] == student_id:
            final_grade = 0.6 * s[2] + 0.4 * s[3]
            print(f"ID: {s[0]}, Name: {s[1][0]} {s[1][1]}, Class Standing: {s[2]}, Major Exam: {s[3]}, Final Grade: {final_grade:.2f}")
            return
    print("Student not found.")

def edit_record():
    student_id = input("Enter Student ID to edit: ")
    for i, s in enumerate(students):
        if s[0] == student_id:
            first_name = input(f"Enter new First Name ({s[1][0]}): ") or s[1][0]
            last_name = input(f"Enter new Last Name ({s[1][1]}): ") or s[1][1]
            try:
                class_standing = float(input(f"Enter new Class Standing ({s[2]}): ") or s[2])
                major_exam = float(input(f"Enter new Major Exam Grade ({s[3]}): ") or s[3])
            except ValueError:
                print("Grades must be numeric.")
                return
            students[i] = (student_id, (first_name, last_name), class_standing, major_exam)
            print("Student record updated.")
            save_file()
            return
    print("Student not found.")

def delete_record():
    student_id = input("Enter Student ID to delete: ")
    global students
    students = [s for s in students if s[0] != student_id]
    print("Student record deleted if it existed.")
    save_file()

def main():
    while True:
        print("\nStudent Record Management System")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Show Student Record")
        print("6. Add Record")
        print("7. Edit Record")
        print("8. Delete Record")
        print("9. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            open_file()
        elif choice == "2":
            save_file()
        elif choice == "3":
            save_as_file()
        elif choice == "4":
            show_all_students()
        elif choice == "5":
            show_student()
        elif choice == "6":
            add_record()
        elif choice == "7":
            edit_record()
        elif choice == "8":
            delete_record()
        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

main()