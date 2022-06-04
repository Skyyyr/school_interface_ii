from staff import Staff
from student import Student
import csv

STUDENT_FILE = "data/students.csv"


class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        with open(STUDENT_FILE, newline='') as file:
            rows_in_file = csv.DictReader(file)
            students = []
            output = "** All Students **\n"
            number_for_list = 1
            for row in rows_in_file:
                students.append(Student(**row))
                output += f"{number_for_list}. {row['name']} {row['school_id']}\n"
                number_for_list += 1
            return print(output)

    def find_student_by_id(self, student_id):
        output = "** Student Look-up Results **\n"
        found_student = False
        for student in self.students:
            current_student = student.__dict__
            if current_student['school_id'] == student_id:
                output += f"{student}"
                found_student = True
                break
        if not found_student:
            return "No student could be found with that ID"
        return print(output)
