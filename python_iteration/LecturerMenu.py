from LecturerController import LecturerController

from Course import Course
from TimeInterval import TimeInterval
from MandatoryCourse import MandatoryCourse
from TechnicalElectiveCourse import TechnicalElectiveCourse
from NonTechnicalElectiveCourse import NonTechnicalElectiveCourse

from Menu import Menu

class LecturerMenu:
    def __init__(self, lecturer_controller=None):
        self.lecturer_controller = lecturer_controller if lecturer_controller else LecturerController()

    def show_given_courses(self):
        for course in self.lecturer_controller.get_lectured_courses():
            print(course)

    def show_students(self):
        for course in self.lecturer_controller.get_lectured_courses():
            for student in self.lecturer_controller.view_enrolled_students(course):
                print(student.get_full_name())

    def lecturer_menu(self):
        choice = 0
        while choice > 4 or choice < 1:
            print("1- Show Given Courses")
            print("2- Show Students that take the given courses")
            print("3- Create Course")
            print("4- Exit")
            print("Enter your choice: ")

            try:
                choice = int(input())
                if choice == 1:
                    self.show_given_courses()
                elif choice == 2:
                    self.show_students()
                elif choice == 3:
                    self.create_course()
                elif choice == 4:
                    Menu.getInstance().set_logged_in_user(None)
                    Menu.getInstance().login_menu()
                else:
                    print("Invalid choice")
            except ValueError:
                print("Invalid input type. Please try again.")
            except Exception as e:
                print(e)

            if choice > 4 or choice < 0:
                print("Input is not valid. Please try again.")
            choice = 0

    def create_course(self):
        try:
            print("Enter the course code")
            print("eg: CSE1001")
            print("eg: -1 to exit")
            course_code = input()
            if course_code == "-1":
                return

            print("Enter the course name")
            print("eg: Introduction to Computer Science")
            course_name = input()

            print("Enter the course description")
            print("eg: This course is an introduction to computer science")
            course_description = input()

            print("Enter the course prerequisites")
            print("eg: CSE101,CSE102")
            course_prerequisites = input().split(',')

            print("Enter the course semester")
            print("eg: 1")
            course_semester = int(input())

            print("Enter the course credit")
            print("eg: 3")
            course_credit = int(input())

            print("Enter the class hours")
            print("eg: 3")
            course_class_hours = int(input())

            print("Enter the course type")
            print("\t 1. Mandatory")
            print("\t 2. Technical Elective")
            print("\t 3. NonTechnical Elective")
            course_type = int(input())

            course = Course(course_code, course_name, course_description, course_prerequisites, course_semester,
                            course_credit, course_class_hours)

            print("Enter the course section name")
            print("eg: 1.1")
            section_name = input()

            print("Enter the course quota")
            print("eg: 30")
            quota = int(input())

            print("Enter the course location")
            print("eg: M1Z11")
            location = input()

            dates = []
            while True:
                print("Enter the course day")
                print("eg: Monday, Tuesday, Wednesday, Thursday or Friday(only one day)")
                print("eg: -1 to exit from time interval adding")
                day = input()
                if day == "-1":
                    break

                print("Enter the course start time")
                print("eg: 09:30, 10:30, 11:30, 13:00, 14:00, 15:00, 16:00(only one time)")
                start_time = input()
                end_time = ""
                if start_time in ["09:30", "10:30", "11:30", "13:00", "14:00", "15:00", "16:00"]:
                    end_time = {
                        "09:30": "10:20",
                        "10:30": "11:20",
                        "11:30": "12:20",
                        "13:00": "13:50",
                        "14:00": "14:50",
                        "15:00": "15:50",
                        "16:00": "16:50"
                    }[start_time]
                else:
                    print("Invalid time")
                    continue

                dates.append(TimeInterval(day, start_time, end_time))

            if course_type == 1:
                print("Enter the course lab hours")
                print("eg: 3")
                print("eg: 0 if there is no lab hours")
                lab_hours = int(input())
                mandatory_course = MandatoryCourse(course, dates, section_name, None, quota, location, lab_hours)
                self.lecturer_controller.add_lectured_course(mandatory_course)

            elif course_type == 2:
                print("Enter the course required credit")
                print("eg: 60")
                required_credit = int(input())
                technical_elective_course = TechnicalElectiveCourse(course, dates, section_name, None, quota, location,
                                                                    required_credit)
                self.lecturer_controller.add_lectured_course(technical_elective_course)

            elif course_type == 3:
                print("Enter the remote or not")
                print("eg: true or false")
                is_remote = input().lower() == 'true'
                non_technical_elective_course = NonTechnicalElectiveCourse(course, dates, section_name, None, quota,
                                                                            location, is_remote)
                self.lecturer_controller.add_lectured_course(non_technical_elective_course)

            else:
                print("Invalid course type")

        except Exception as e:
            print(e)
