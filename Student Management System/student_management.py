import json
import os

# Student Class
class Student:
    def __init__(self, student_id, name, age, grade, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.course = course

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
            "course": self.course
        }

# Student Management System

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    # CREATE
    
    def add_student(self, student):
        # Prevent duplicate ID
        for s in self.students:
            if s.student_id == student.student_id:
                print("Student ID already exists!")
                return
        self.students.append(student)
        print("Student added successfully!")

    # READ
    def view_students(self):
        if not self.students:
            print("No students available.")
            return

        print("\n--- Student List ---")
        print("{:<10} {:<20} {:<5} {:<10} {:<15}".format(
            "ID", "Name", "Age", "Grade", "Course"))
        print("-" * 65)

        for student in self.students:
            print("{:<10} {:<20} {:<5} {:<10} {:<15}".format(
                student.student_id,
                student.name,
                student.age,
                student.grade,
                student.course
            ))

    # UPDATE
    def update_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print("Enter new details:")

                name = input("Name: ")
                age = input("Age: ")
                grade = input("Grade: ")
                course = input("Course: ")

                if not validate_age(age):
                    print("Invalid age. Update cancelled.")
                    return

                student.name = name
                student.age = int(age)
                student.grade = grade
                student.course = course

                print("Student updated successfully!")
                return

        print("Student not found.")

    # DELETE
    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student deleted successfully!")
                return
        print("Student not found.")

    # SEARCH
    def search_student(self, keyword):
        found = False
        for student in self.students:
            if keyword.lower() in student.name.lower() or keyword == student.student_id:
                print(student.to_dict())
                found = True

        if not found:
            print("No matching student found.")

    # SORT STUDENTS
    def sort_students(self, key):
        if key == "name":
            self.students.sort(key=lambda x: x.name.lower())
        elif key == "grade":
            self.students.sort(key=lambda x: x.grade)
        elif key == "age":
            self.students.sort(key=lambda x: x.age)
        else:
            print("Invalid sort key.")
            return

        print(f"Students sorted by {key} successfully!")

    # SAVE TO JSON
    def save_to_file(self, filename="students.json"):
        with open(filename, "w") as file:
            json.dump([s.to_dict() for s in self.students], file, indent=4)
        print("Data saved successfully!")

    # LOAD FROM JSON
    def load_from_file(self, filename="students.json"):
        if not os.path.exists(filename):
            return

        with open(filename, "r") as file:
            data = json.load(file)
            self.students = [Student(**item) for item in data]

        print("📂 Data loaded successfully!")


# Validation Function
def validate_age(age):
    return age.isdigit() and 5 <= int(age) <= 100


def validate_name(name):
    return name.replace(" ", "").isalpha()


# Main Menu
def main():
    sms = StudentManagementSystem()
    sms.load_from_file()

    while True:
        print("\n====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Sort Students")
        print("7. Save & Exit")

        choice = input("Enter your choice: ")

        # ADD
        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            grade = input("Enter Grade: ")
            course = input("Enter Course: ")

            if not validate_name(name):
                print("Invalid name! Only letters allowed.")
                continue

            if not validate_age(age):
                print("Invalid age! Age must be between 5 and 100.")
                continue

            student = Student(student_id, name, int(age), grade, course)
            sms.add_student(student)

        # VIEW
        elif choice == "2":
            sms.view_students()

        # UPDATE
        elif choice == "3":
            sid = input("Enter Student ID to update: ")
            sms.update_student(sid)

        # DELETE
        elif choice == "4":
            sid = input("Enter Student ID to delete: ")
            sms.delete_student(sid)

        # SEARCH
        elif choice == "5":
            keyword = input("Enter ID or Name to search: ")
            sms.search_student(keyword)

        # SORT
        elif choice == "6":
            key = input("Sort by (name/grade/age): ")
            sms.sort_students(key)

        # EXIT
        elif choice == "7":
            sms.save_to_file()
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()