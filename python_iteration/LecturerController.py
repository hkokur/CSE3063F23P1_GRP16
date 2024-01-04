from typing import List

from Course import Course
from Lecturer import Lecturer
from Student import Student


class LecturerController:
    def __init__(self, lecturer: Lecturer = None):
        self.lecturer = lecturer

    def get_lectured_courses(self) -> List[Course.Course]:
        return self.lecturer.get_lectured_courses()

    def add_lectured_course(self, course: Course) -> bool:
        return self.lecturer.add_lectured_courses(course)

    def delete_lectured_courses(self, course: Course) -> bool:
        return self.lecturer.delete_lectured_courses(course)

    def view_enrolled_students(self, course: Course) -> List[Student.Student]:
        return self.lecturer.view_enrolled_students(course)

