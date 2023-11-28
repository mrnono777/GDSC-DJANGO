students_database = {}

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")

    student_info = {'Name': name, 'Age': age, 'Grade': grade}
    students_database[name] = student_info
    print(f"{name} has been added to the database.\n")

def view_student():
    name = input("Enter student name to view details: ")
    if name in students_database:
        print(f"\nStudent Details for {name}:")
        for key, value in students_database[name].items():
            print(f"{key}: {value}")
        print()
    else:
        print(f"\nStudent {name} not found in the database.\n")

def list_all_students():
    print("\nList of All Students:")
    for name, info in students_database.items():
        print(f"Name: {name}, Age: {info['Age']}, Grade: {info['Grade']}")
    print()

def update_student():
    name = input("Enter student name to update information: ")
    if name in students_database:
        print(f"\nCurrent Details for {name}:")
        for key, value in students_database[name].items():
            print(f"{key}: {value}")

        age = int(input("\nEnter new age (press Enter to keep current age): ") or students_database[name]['Age'])
        grade = input("Enter new grade (press Enter to keep current grade): ") or students_database[name]['Grade']

        students_database[name]['Age'] = age
        students_database[name]['Grade'] = grade

        print(f"\nInformation updated for {name}.\n")
    else:
        print(f"\nStudent {name} not found in the database.\n")

def delete_student():
    name = input("Enter student name to delete from the database: ")
    if name in students_database:
        del students_database[name]
        print(f"\n{name} has been deleted from the database.\n")
    else:
        print(f"\nStudent {name} not found in the database.\n")

def student_list():
    while True:
        print("Student Database")
        print("1. Add Student")
        print("2. View Student")
        print("3. List All Students")
        print("4. Update Student Information")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_student()
        elif choice == '3':
            list_all_students()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__student_list__":
    student_list()