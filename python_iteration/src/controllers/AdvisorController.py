from typing import List
from models import Advisor, Student, Course

class AdvisorController:
    def __init__(self, advisor: Advisor):
        self.advisor = advisor

    def get_students(self) -> List[Student.Student]:
        return self.advisor.get_students()

    def add_student(self, student: Student):
        self.advisor.add_student(student)

    def delete_student(self, student: Student):
        self.advisor.delete_student(student)

    def student_course_organization(self, student: Student):
        self.advisor.student_course_organization(student)

    def get_combined_courses(self, student: Student) -> List[Course.Course]:
        return self.advisor.get_combined_courses(student)

    def approve_student_selection(self, student: Student, selections: List[int]) -> bool:
        return self.advisor.approve_student(student, selections)

    def reject_student_selection(self, student: Student, selections: str) -> bool:
        try:
            return self.advisor.reject_student(student, selections)
        except Exception as e:
            raise e
