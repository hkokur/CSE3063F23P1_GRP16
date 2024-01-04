from controllers import StudentController
from models import Course, Transcript
from menus import Menu

import logging

class StudentMenu:
    # Logger
    logging.basicConfig(filename='iteration_2/logs/mylog.log',
                        level=logging.INFO,
                        format='%(asctime)s %(levelname)-5s %(name)s:%(lineno)d - %(message)s')

    def __init__(self, student_controller):
        self.student_controller = student_controller

    def student_menu(self):
        logging.info("Student menu displayed")
        choice = 0
        while choice != 6:
            print("1-Add Course")
            print("2-Drop Course")
            print("3-Show Transcript")
            print("4-Show Selected Courses")
            print("5-Send Approval Request")
            print("6-Logout")
            try:
                choice = int(input("Enter your choice: "))
                self.handle_menu_choice(choice)
            except ValueError:
                print("Invalid input type. Please try again.")

    def handle_menu_choice(self, choice):
        if choice == 1:
            self.course_adding()
        elif choice == 2:
            self.course_dropping()
        elif choice == 3:
            self.show_transcript()
        elif choice == 4:
            self.show_selected_courses()
        elif choice == 5:
            self.send_approval_request()
        elif choice == 6:
            Menu.get_instance().set_logged_in_user(None)
            Menu.get_instance().login_menu()
        else:
            print("Invalid choice")

    def course_adding(self):
        logging.info("Course adding menu displayed")
        self.show_available_courses()

        print("Enter the course you want to add")
        print("eg: 1,2,3")
        print("eg: * for all courses")
        print("eg: -1 to exit")
        try:
            input_str = input()
            selected_courses = self.parse_input(input_str, self.student_controller.get_available_courses())
            for index in selected_courses:
                self.student_controller.add_course(self.student_controller.get_available_courses()[index - 1])
        except Exception as e:
            print(f"Error: {e}")

    def course_dropping(self):
        logging.info("Course dropping menu displayed")
        self.show_selected_courses()

        print("Enter the course you want to drop")
        print("eg: 1,2,3")
        print("eg: * for all courses")
        print("eg: -1 to exit")
        try:
            input_str = input()
            selected_courses = self.parse_input(input_str, self.student_controller.get_selected_courses())
            for index in reversed(selected_courses):
                self.student_controller.drop_course(self.student_controller.get_selected_courses()[index - 1])
        except Exception as e:
            print(f"Error: {e}")

    def show_selected_courses(self):
        logging.info("Selected courses displayed")
        courses = self.student_controller.get_selected_courses()
        print(f"Status: {self.student_controller.get_status()}")
        print("=============Selected Courses=============")

        for i, course in enumerate(courses, start=1):
            print(f"{i}-{course.get_full_name()} [{course.get_short_name()}] ({course.get_credit()})")

        print("============================================")

    def show_available_courses(self):
        logging.info("Available courses displayed")
        courses = self.student_controller.get_available_courses()
        print("=============Available Courses=============")

        for i, course in enumerate(courses, start=1):
            print(f"{i}-{course.get_full_name()} [{course.get_short_name()}] ({course.get_credit()})")

        print("============================================")

    def show_transcript(self):
        logging.info("Transcript displayed")
        transcript = self.student_controller.get_transcript()
        grades = transcript.get_grades()

        print("=================Transcript==================")
        print(grades)
        print("=============================================")

    def send_approval_request(self):
        logging.info("Approval request sent")
        if self.student_controller.send_approval_request():
            print("Approval request sent")
        else:
            print("Approval request could not be sent")

    @staticmethod
    def parse_input(input_str, courses):
        selected_courses = []

        if input_str == "*":
            selected_courses = list(range(1, len(courses) + 1))
        elif input_str == "-1":
            # Exit the course selection process
            # No need to add any courses
            pass
        else:
            input_list = input_str.split(",")
            for item in input_list:
                try:
                    index = int(item)
                    if 0 < index <= len(courses):
                        selected_courses.append(index)
                except ValueError:
                    raise ValueError("Invalid input")

        return selected_courses
