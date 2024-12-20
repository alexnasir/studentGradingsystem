###Author
Alex

##Done on date:
20/12/2024

###Student and Grade Management System

This project is a Python-based Student and Grade Management System that uses SQLAlchemy for database interactions. The application allows managing students and their grades through a command-line interface (CLI).

###Features

##Student Management

#Add Student: Create a new student record with name and email.

#Delete Student: Remove a student by their ID.

#View All Students: List all students with their details and average grades.

#Find Student by ID: Retrieve detailed information about a specific student.

#Grade Management

#Add Grade: Assign a grade to a student for a specific subject.

#View Grades: List all grades with student information, subject, and scores.

###Database Models

##Student:

id: Integer (Primary Key)

name: String (Required)

email: String (Unique, Required)

grades: Relationship with Grade


####Author

Alex
##Grade:

id: Integer (Primary Key)

student_id: Integer (Foreign Key to Student.id, Cascade on Delete)

subject: String (Required)

score: Float (Required, Range 0-100)

student: Relationship with Student

###Getting Started

Prerequisites

Python 3.7+

SQLAlchemy library

A database engine (e.g., SQLite, PostgreSQL, MySQL)

###Setup

Clone the repository:

git clone https://github.com/alex/student-grade-management.git

Install dependencies:

pip install sqlalchemy

Configure the database connection in models/base.py.

Run database migrations to create the necessary tables.

Running the Application

To launch the student management menu:

python manage.py student_menu

To launch the grade management menu:

python manage.py grade_menu

###Code Structure

student-grade-management/
├── models/
│   ├── base.py         # Database configuration and session management
│   ├── grade.py        # Grade model definition
│   ├── student.py      # Student model definition
├── manage.py           # CLI for interacting with the application
├── README.md           # Project documentation


###License

This project is licensed under the MIT License - see the LICENSE file for details.

