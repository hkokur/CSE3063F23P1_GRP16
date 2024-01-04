from StudentController import StudentController
from AdvisorController import AdvisorController
from LecturerController import LecturerController
from Student import Student
from Advisor import Advisor
from Lecturer import Lecturer
from DataUtils import DataUtils


import logging
from logging import handlers

class Menu:
    # Logger
    logging.basicConfig(filename='iteration_2/logs/mylog.log',
                        level=logging.INFO,
                        format='%(asctime)s %(levelname)-5s %(name)s:%(lineno)d - %(message)s')

    # Singleton
    menu_instance = None

    @staticmethod
    def get_instance():
        if Menu.menu_instance is None:
            Menu.menu_instance = Menu()
        return Menu.menu_instance

    def __init__(self):
        self.logged_in_user = None
        self.json = DataUtils()
        self.lecturers = self.json.read_lecturers()
        self.students = self.json.read_students()
        self.advisors = self.json.read_advisors()

    def login_menu(self):
        while self.logged_in_user is None:
            logging.info("Login menu displayed")
            print("Welcome to the Course Management System!")
            print("Please enter your username and password to login.")
            username = input("Username: ")
            password = input("Password: ")
            is_logged = self.authenticate(username, password)
            if is_logged:
                print("Login successful!")
                logging.info(f"User {username} logged in successfully")
            else:
                print("Login unsuccessful!\n")
                logging.warn(f"User {username} failed to log in with username {username} and password {password}")
        self.person_menu()

    def person_menu(self):
        if isinstance(self.logged_in_user, Student):
            student_menu = StudentMenu(StudentController(self.logged_in_user))
            student_menu.student_menu()
        elif isinstance(self.logged_in_user, Advisor):
            advisor_menu = AdvisorMenu(AdvisorController(self.logged_in_user))
            advisor_menu.advisor_menu()
        elif isinstance(self.logged_in_user, Lecturer):
            lecturer_menu = LecturerMenu(LecturerController(self.logged_in_user))
            lecturer_menu.lecturer_menu()

    def authenticate(self, username, password):
        for student in self.students:
            if student.username == username and student.password == password:
                self.logged_in_user = student
                return True
        for lecturer in self.lecturers:
            if lecturer.username == username and lecturer.password == password:
                self.logged_in_user = lecturer
                return True
        for advisor in self.advisors:
            if advisor.username == username and advisor.password == password:
                self.logged_in_user = advisor
                return True
        return False


class StudentMenu:
    def __init__(self, student_controller):
        self.student_controller = student_controller

    def student_menu(self):
        pass  # Implement student menu logic here


class AdvisorMenu:
    def __init__(self, advisor_controller):
        self.advisor_controller = advisor_controller

    def advisor_menu(self):
        pass  # Implement advisor menu logic here


class LecturerMenu:
    def __init__(self, lecturer_controller):
        self.lecturer_controller = lecturer_controller

    def lecturer_menu(self):
        pass  # Implement lecturer menu logic here
