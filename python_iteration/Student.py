from Person import Person
from Course import Course
from Transcript import Transcript
from Grade import Grade
from TimeInterval import TimeInterval
from DataUtils import DataUtils
from Menu import Menu

class Student(Person):
    def __init__(self, name, surname, id, password, address, phone_number, semester, entrance_year, status, selected_courses, transcript):
        super().__init__(name, surname, id, password)
        self.address = address
        self.phone_number = phone_number
        self.semester = semester
        self.entrance_year = entrance_year
        self.status = status
        self.selected_courses = selected_courses
        self.transcript = transcript

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_semester(self):
        return self.semester

    def set_semester(self, semester):
        self.semester = semester

    def get_entrance_year(self):
        return self.entrance_year

    def set_entrance_year(self, entrance_year):
        self.entrance_year = entrance_year

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def get_selected_courses(self):
        return self.selected_courses

    def set_selected_courses(self, selected_courses):
        self.selected_courses = selected_courses

    def get_transcript(self):
        return self.transcript

    def set_transcript(self, transcript):
        self.transcript = transcript

    def add_course(self, course):
        if self.status in ["waiting", "finished"]:
            print(f"Error: Student can't add/drop course in {self.status} statement")
            return False

        if len(self.selected_courses) >= 5:
            print("Error: Student can't add more than 5 courses")
            return False

        try:
            self.selected_courses.append(course)

            database = DataUtils.get_instance()
            database.write_students(Menu.students)

            # Update the advisor's student's selected courses
            advisors = database.read_advisors()
            for advisor in advisors:
                for j, student in enumerate(advisor.students):
                    if student.username == self.username:
                        advisor.students[j] = self

            database.write_advisors(advisors)

            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def drop_course(self, course):
        if self.status in ["waiting", "finished"]:
            print(f"Error: Student can't add/drop course in {self.status} statement")
            return False

        try:
            self.selected_courses.remove(course)

            database = DataUtils.get_instance()
            database.write_students(Menu.students)

            # Update the advisor's student's selected courses
            advisors = database.read_advisors()
            for advisor in advisors:
                for j, student in enumerate(advisor.students):
                    if student.username == self.username:
                        advisor.students[j] = self

            database.write_advisors(advisors)

            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def get_available_courses(self):
        available_courses = []

        all_courses = self.get_all_courses()
        for course in all_courses:
            if self.student_can_take_course(course):
                available_courses.append(course)

        return available_courses

    def student_can_take_course(self, course):
        if not self.check_student_already_selected_course(course) and \
                self.check_prerequisite(course) and \
                self.check_semester_of_course(course) and \
                not self.check_student_passed_course(course):
            return True
        else:
            return False

    def get_all_courses(self):
        all_courses = []

        data_utils = DataUtils.get_instance()
        all_courses.extend(data_utils.read_mandatory_courses())
        all_courses.extend(data_utils.read_technical_elective_course())
        all_courses.extend(data_utils.read_non_technical_elective_courses())

        return all_courses

    def get_warnings(self):
        warning_string = ""

        if not self.check_credit_limit():
            warning_string += "========Student has exceeded the credit limit.==========\n"
            warning_string += f"Total credit: {self.get_total_credit_of_selected_courses()}\n"
            warning_string += "Max credit: 30\n"
            warning_string += "========================================================\n"

        return warning_string

    def send_approval_request(self):
        if self.status in ["waiting", "finished"]:
            print(f"Error: Student can't send for approval in {self.status} statement")
            return False

        self.status = "waiting"
        database = DataUtils.get_instance()
        database.write_students(Menu.students)
        return True

    def get_total_credit_of_selected_courses(self):
        total_credit = 0

        for course in self.selected_courses:
            total_credit += course.credit

        return total_credit

    def check_credit_limit(self):
        return self.get_total_credit_of_selected_courses() <= 30

    def check_student_already_selected_course(self, course):
        return any(selected_course.short_name == course.short_name for selected_course in self.selected_courses)

    def check_prerequisite(self, course):
        if not course.prerequisite:
            return True
        else:
            return all(self.check_student_passed_course_with_short_name(prerequisite) for prerequisite in course.prerequisite)

    def check_semester_of_course(self, course):
        return course.semester <= self.semester

    def check_student_passed_course(self, course):
        return any(grade.course.short_name == course.short_name and grade.grade != "FF" for grade in self.transcript.grade_list)

    def check_student_passed_course_with_short_name(self, course_short_name):
        return any(grade.course.short_name == course_short_name and grade.grade != "FF" for grade in self.transcript.grade_list)

    def get_overlapping_courses(self):
        overlapping_courses = []

        for i in range(len(self.selected_courses)):
            for j in range(i + 1, len(self.selected_courses)):
                for time_interval in self.selected_courses[i].get_dates():
                    for time_interval2 in self.selected_courses[j].get_dates():
                        try:
                            if time_interval.is_overlapping(time_interval2):
                                overlapping_course = [self.selected_courses[i], self.selected_courses[j]]
                                overlapping_courses.append(overlapping_course)
                        except Exception as e:
                            print(e)

        return overlapping_courses
