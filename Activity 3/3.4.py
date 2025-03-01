try:
    with open("Activity 3/students.txt", "r") as file:
        student_data = file.read()

        if not student_data.strip():
            print("No student information found in 'students.txt'.")
        else:
            print("\nReading Student Information:\n")
            print(student_data)

except FileNotFoundError:
    print("The file 'students.txt' does not exist. Please add student information first.")