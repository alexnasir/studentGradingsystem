from models.base import session
from models.grade import Grade
from models.student import Student

def grade_menu():
    while True:
        print("\nGrade Menu")
        print("1. Add Grade")
        print("2. View Grades")
        print("3. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            add_grade()
        elif choice == "2":
            view_grades()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def add_grade():
    student_id = input("Enter student ID: ")
    student = session.query(Student).get(student_id)
    if not student:
        print("Error: Student not found.")
        return

    subject = input("Enter subject: ")
    score = float(input("Enter score (0-100): "))
    if score < 0 or score > 100:
        print("Error: Invalid score. Must be between 0 and 100.")
        return

    grade = Grade(student=student, subject=subject, score=score)
    session.add(grade)
    session.commit()
    print(f"Grade '{subject}: {score}' added for {student.name}.")

def view_grades():
    grades = session.query(Grade).all()
    if not grades:
        print("No grades found.")
        return
    for grade in grades:
        print(f"ID: {grade.id}, Student: {grade.student.name}, Subject: {grade.subject}, Score: {grade.score}")
