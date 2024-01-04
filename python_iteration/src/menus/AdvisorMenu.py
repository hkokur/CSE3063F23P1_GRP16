from models import Student, Course
from menus import Menu
from constants import String_Constants

class AdvisorMenu:
    def __init__(self, advisor_controller):
        self.advisor_controller = advisor_controller
        self.scanner = input

    def advisor_menu(self):
        student_selection = 0

        while student_selection < 1 or student_selection > len(self.advisor_controller.get_students()):
            print("Which student do you want to go on?\n"
                  + "Type -1 for exit")
            for j, student in enumerate(self.advisor_controller.get_students()):
                print(f"{j + 1}- {student.get_full_name()}", end='')
                if student.get_status() == "Rejected":
                    print(" (Rejected)")
                elif student.get_status() == "Approved":
                    print(" (Approved)")
                elif student.get_status() == "Waiting":
                    print(" (Waiting)")
                else:
                    print()

            try:
                student_selection = int(input())
            except ValueError:
                print("Invalid choice. Please try again.")

        if student_selection == -1:
            menu = Menu()
            menu.login_menu()
            return

        student = self.advisor_controller.get_students()[student_selection - 1]

        print("List of courses for student " + student.get_full_name())

        courses_of_student = student.get_selected_courses()
        if student.get_status() == "Rejected" or student.get_status() == "Approved":
            print("Approve/Reject process is already done for this student.\n")
        else:
            for i, course in enumerate(courses_of_student):
                print(f"{i + 1} -> {course.get_full_name()} {course.get_short_name()}")

            print("Please enter the courses you want to approve for the student \n"
                  + "Type * to approve all courses\n"
                  + "The non-chosen ones will automatically be rejected\n"
                  + "Type -1 for exit\n"
                  + "Selection/s: ")

            selections = input()

            if selections == "-1":
                self.advisor_menu()
                return

            sorted_selections = []

            while True:
                if selections == "*":
                    sorted_selections.append(0)
                    self.advisor_controller.approve_student_selection(student, sorted_selections)
                    break
                else:
                    if not self.is_valid_format(selections):
                        print("Invalid format. Please enter a valid comma-separated list of numbers.\n")
                    else:
                        sorted_selections = self.sort_numbers(selections)

                        if sorted_selections[0] <= 0:
                            print("Invalid input. Please stay in bounds.\n")
                        else:
                            self.advisor_controller.approve_student_selection(student, sorted_selections)
                            break

                    print("Enter a comma-separated list of numbers: ")
                    selections = input()

        self.advisor_menu()

    def is_valid_format(self, selections):
        selections = selections.replace("[,\\s]", "")

        try:
            int_value = int(selections)
            return True
        except ValueError:
            print("Exception: Invalid input.\n")
            return False

    def sort_numbers(self, input):
        number_strings = input.split(",")
        numbers = [int(number_string) for number_string in number_strings]

        numbers.sort()
        return numbers
