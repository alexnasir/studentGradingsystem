from models.base import session
from models.student import Student

def student_menu():
    while True:
        print("\nStudent Menu")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. View All Students")
        print("4. Find Student by ID")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            delete_student()
        elif choice == "3":
            view_students()
        elif choice == "4":
            find_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def add_student():
    name = input("Enter student name: ")
    email = input("Enter student email: ")
    if session.query(Student).filter_by(email=email).first():
        print("Error: Email already exists!")
        return
    student = Student(name=name, email=email)
    session.add(student)
    session.commit()
    print(f"Student '{name}' added successfully!")

def view_students():
    students = session.query(Student).all()
    if not students:
        print("No students found.")
        return
    for student in students:
        print(f"ID: {student.id}, Name: {student.name}, Email: {student.email}, Avg Grade: {student.average_grade:.2f}")

def delete_student():
    student_id = input("Enter student ID to delete: ")
    try:
        
        student = session.query(Student).filter_by(id=int(student_id)).first()
        if student:
            session.delete(student)
            session.commit()
            print(f"Student with ID {student_id} has been deleted.")
        else:
            print(f"No student found with ID {student_id}.")
    except Exception as e:
        session.rollback()
        print(f"Error deleting student: {e}")


def find_student():
    student_id = input("Enter student ID to find: ")
    try:
        student_id = int(student_id)
        student = session.query(Student).filter_by(id=student_id).first()
        if not student:
            print(f"No student found with ID {student_id}.")
            return
        print(f"ID: {student.id}, Name: {student.name}, Email: {student.email}, Avg Grade: {student.average_grade:.2f}")
    except ValueError:
        print("Invalid ID. Please enter a valid integer.")
