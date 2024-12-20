#!/usr/bin/python3


from models.base import create_tables
from cli.student_cli import student_menu
from cli.grade_cli import grade_menu

create_tables()


def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Manage Students")
        print("2. Manage Grades")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            student_menu()
        elif choice == "2":
            grade_menu()
        elif choice == "3":
            print("Exiting 🖐️✨.Thank you for using studentGradingsystem!!!!!! Goodbye🎉🎊🎈!")
            break
        else:
            print("Invalid choice. Please try again😄.")

if __name__ == "__main__":
    main_menu()
    
    
