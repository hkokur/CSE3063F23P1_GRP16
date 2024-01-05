from typing import List

from Person import Person
from Course import Course
from Transcript import Transcript
import logging

from CourseSection import CourseSection

# Configuring logging
logging.basicConfig(
    filename="logs.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
)
logger = logging.getLogger(__name__)

# Global variables
MAX_COURSES = 5
MAX_CREDIT_LIMIT = 30
PRIMARY_COLOR = "magenta"
SECONDARY_COLOR = "black"
TEXT_COLOR = "white"
EXIT_COLOR = "red"
INPUT_COLOR = "yellow"


# Not: Course can be CourseSection


class Student(Person):
    def __init__(
        self,
        firstName: str,
        lastName: str,
        username: str,
        password: str,
        semester: int,
        status: str,
        waitingCourses: List[CourseSection],
        approvedCourses: List[CourseSection],
        rejectedCourses: List[CourseSection],
        transcript: Transcript,
    ):
        super().__init__(firstName, lastName, username, password)
        self.__semester = semester
        self.__status = status
        self.__waitingCourses = waitingCourses
        self.__approvedCourses = approvedCourses
        self.__rejectedCourses = rejectedCourses
        self.__transcript = transcript

    # getters and setters
    @property
    def semester(self):
        return self.__semester

    @semester.setter
    def semester(self, semester: int):
        self.__semester = semester

    @property
    def enteranceYear(self):
        return self.__enteranceYear

    @enteranceYear.setter
    def enteranceYear(self, enteranceYear: int):
        self.__enteranceYear = enteranceYear

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    def addwaitingCourses(self, course: CourseSection):
        self.__waitingCourses.append(course)

    def removewaitingCourses(self, course: CourseSection):
        # TODO: implement, can be __eq__ method use in the Course class or
        # use while loop and check the course name etc.
        pass

    def addapprovedCourses(self, course: CourseSection):
        self.__approvedCourses.append(course)

    def removeapprovedCourses(self, course: Course):
        # TODO: implement, can be __eq__ method use in the Course class or
        # use while loop and check the course name etc.
        pass

    def addrejectedCourses(self, course: CourseSection):
        self.__rejectedCourses.append(course)

    def removerejectedCourses(self, course: CourseSection):
        # TODO: implement, can be __eq__ method use in the Course class or
        # use while loop and check the course name etc.
        pass

    def printwaitingCourses(self):
        print("SELECTED COURSES:")
        for index, course in enumerate(self.__waitingCourses):
            print(f"{index+1}. {course.get_full_name()}")

    def printapprovedCourses(self):
        print("APPROVED COURSES:")
        for index, course in enumerate(self.__approvedCourses):
            print(f"{index+1}. {course.get_full_name()}")

    def printrejectedCourses(self):
        print("REJECTED COURSES:")
        for index, course in enumerate(self.__rejectedCourses):
            print(f"{index+1}. {course.get_full_name()}")

    def printTranscript(self):
        print("TRANSCRIPT:")
        # TODO: implement, writing __str__ in transcript class
        print(self.__transcript)

    # Add course to waiting list
    def addCourse(self, course: CourseSection):
        # Check if course is already in waiting list
        if course in self.__waitingCourses:
            print("Course already in waiting list")
            return

        # Check if student has exceeded the maximum number of courses
        if len(self.__waitingCourses) == MAX_COURSES:
            print("Maximum number of courses exceeded")
            return

        try:
            # Add course to waiting list
            self.__waitingCourses.append(course)

            logger.info(
                f"Course {course.get_full_name()} added to waiting list of {self.getFullName()}"
            )
        except:
            print("Error adding course")
            logger.error("Error adding course")

    # Drop course from waiting list
    def dropCourse(self, course: CourseSection):
        try:
            # Remove course from waiting list
            self.__waitingCourses.remove(course)
            logger.info(
                f"Course {course.getFullName()} dropped from waiting list of {self.getFullName()}"
            )
        except:
            print("Error dropping course")
            logger.error("Error dropping course")

    # Available Courses
    """
    If course is not in waiting list, approved list or rejected list or courses that student has already passed

    If student has passed prerequisites
    """

    def getAvailableCourses(self):
        availableCourses = []

        # Getting all courses from database
        dataUtils = DataUtils.get_instance()
        allCourses = dataUtils.get_courses()

        for course in allCourses:
            if self.__canStudentTakeCourse(course):
                availableCourses.append(course)

        return availableCourses

    # Private helper methods
    def __isCourseInWaitingCoursesList(self, course: CourseSection):
        return course in self.__waitingCourses

    def __isCourseInApprovedCoursesList(self, course: CourseSection):
        return course in self.__approvedCourses

    def __isCourseInRejectedCoursesList(self, course: CourseSection):
        return course in self.__rejectedCourses

    def __isCourseInCurrentCoursesList(self, course: CourseSection):
        return (
            self.__isCourseInWaitingCoursesList(course)
            or self.__isCourseInApprovedCoursesList(course)
            or self.__isCourseInRejectedCoursesList(course)
        )

    def __isStudentAlreadyPassedCourse(self, course: CourseSection):
        return course in self.__transcript.getPassedCourses()

    # Checks passed courses with short names of prerequisites
    def __isStudentPassedPrerequisites(self, course: CourseSection):
        prerequisites = course.getPrerequisites()

        passedCourses_shortNames = [
            passedCourse.getShortName()
            for passedCourse in self.__transcript.getPassedCourses()
        ]

        for prerequisite in prerequisites:
            if prerequisite not in passedCourses_shortNames:
                return False

        return True

    # Checks student's semester with semester of course
    # If student's semester is greater or equal than semester of course, returns True
    def __isStudentHasNeededSemester(self, course: CourseSection):
        return self.__semester >= course.getSemester()

    # Checks if student can take course
    def __canStudentTakeCourse(self, course: CourseSection):
        # Check if course is in current courses list( waiting, approved or rejected courses)
        if self.__isCourseInCurrentCoursesList(course):
            return False

        # Check if student has already passed course
        if self.__isStudentAlreadyPassedCourse(course):
            return False

        # Check if student has passed prerequisites
        if not self.__isStudentPassedPrerequisites(course):
            return False

        # Check if student has needed semester
        if not self.__isStudentHasNeededSemester(course):
            return False

        return True

    # Computes the total number of credits of courses in waiting list
    def getTotalCredits(self):
        totalCredits = 0

        for course in self.__waitingCourses:
            totalCredits += course.getCredit()

        return totalCredits

    def getWarnings(self):
        warnings = []
        if self.getTotalCredits() > MAX_CREDIT_LIMIT:
            warnings.append(colored_string("Maximum credit limit exceeded", "red"))

        return warnings

    # Check overlap between courses in waiting list
    def checkOverlap(self):
        pass

    def getMenu(self):
        MenuString = (
            colored_string(f"Welcome {self.getFullName}", "green")
            + "\n"
            + colored_string("1", PRIMARY_COLOR)
            + colored_string("-", SECONDARY_COLOR)
            + " Add course to waiting list\n"
            + colored_string("2", PRIMARY_COLOR)
            + colored_string("-", SECONDARY_COLOR)
            + " Drop course from waiting list\n"
            + colored_string("3", PRIMARY_COLOR)
            + colored_string("-", SECONDARY_COLOR)
            + " List available courses\n"
            + colored_string("4", PRIMARY_COLOR)
            + colored_string("-", SECONDARY_COLOR)
            + " List waiting courses\n"
            + colored_string("5", PRIMARY_COLOR)
            + colored_string("-", SECONDARY_COLOR)
            + " List approved courses\n"
            + colored_string("6", PRIMARY_COLOR)
            + colored_string("-", SECONDARY_COLOR)
            + " List rejected courses\n"
            + colored_string("7", PRIMARY_COLOR)
            + colored_string("-", SECONDARY_COLOR)
            + " List transcript\n"
            + colored_string("8", PRIMARY_COLOR)
            + colored_string("-", SECONDARY_COLOR)
            + " Exit\n"
            + colored_string("Please select an option: ", "yellow")
        )

        print(MenuString)
        while option < 1 or option > 8:
            try:
                option = int(input())
            except TypeError:
                print("Please enter a valid option")
                continue

            if option == 1:
                self.MENU_ADD_COURSE()
            elif option == 2:
                self.MENU_DROP_COURSE()
            elif option == 3:
                self.MENU_LIST_AVAILABLE_COURSES()
            elif option == 4:
                self.MENU_LIST_WAITING_COURSES()
            elif option == 5:
                self.MENU_LIST_APPROVED_COURSES()
            elif option == 6:
                self.MENU_LIST_REJECTED_COURSES()
            elif option == 7:
                self.MENU_LIST_TRANSCRIPT()
            elif option == 8:
                self.MENU_EXIT()
            else:
                print("Please enter a valid option")
                continue

    def MENU_ADD_COURSE(self):
        availableCourses = self.getAvailableCourses()

        if len(availableCourses) == 0:
            print(colored_string("No available courses", "red"))
            return

        for index, course in enumerate(availableCourses):
            print(
                colored_string(f"{index+1}", PRIMARY_COLOR)
                + colored_string("-", SECONDARY_COLOR)
                + colored_string(f" {course.getFullName()}", TEXT_COLOR)
            )

        print(colored_string("Please select a course: ", INPUT_COLOR))
        option = 0
        while option < 1 or option > len(availableCourses):
            try:
                option = int(input())
            except TypeError:
                print("Please enter a valid option")
                continue

            if option < 1 or option > len(availableCourses):
                print("Please enter a valid option")
                continue

            self.addCourse(availableCourses[option - 1])
            return

    def MENU_DROP_COURSE(self):
        waitingCourses = self.waitingCourses

    def MENU_LIST_AVAILABLE_COURSES(self):
        pass

    def MENU_LIST_WAITING_COURSES(self):
        pass

    def MENU_LIST_APPROVED_COURSES(self):
        pass

    def MENU_LIST_REJECTED_COURSES(self):
        pass

    def MENU_LIST_TRANSCRIPT(self):
        pass

    def MENU_EXIT(self):
        pass

    def getInformation():
        pass

    def getMenu():
        pass

    def toJson(self):
        return {
            "personName": self._Person__personName,
            "personSurname": self._Person__personSurname,
            "username": self._Person__username,
            "password": self._Person__password,
            "semester": self.__semester,
            "status": self.__status,
            "waitingCourses": [
                {
                    "shortName": course_section.short_name,
                    "sectionName": course_section.section_name,
                }
                for course_section in self.__waitingCourses
            ],
            "approvedCourses": [
                {
                    "shortName": course_section.short_name,
                    "sectionName": course_section.section_name,
                }
                for course_section in self.__approvedCourses
            ],
            "rejectedCourses": [
                {
                    "shortName": course_section.short_name,
                    "sectionName": course_section.section_name,
                }
                for course_section in self.__rejectedCourses
            ],
            "transcript": self.__transcript.to_json(),
        }

    # it can be used for writing to json file
    # def write(self):
    #     from DataInitializer import DataInitializer

    #     dataInitializer = DataInitializer()
    #     dataInitializer.write_student(self)


def colored_string(text, color):
    colors = {
        "reset": "\033[0m",
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
    }

    if color not in colors:
        raise ValueError("Geçersiz renk: {}".format(color))

    return colors[color] + text + colors["reset"]


def getMenu():
    return (
        colored_string(f"Welcome BURAK", "green")
        + "\n"
        + colored_string("1", PRIMARY_COLOR)
        + colored_string("-", SECONDARY_COLOR)
        + colored_string(" Add course to waiting list\n", TEXT_COLOR)
        + colored_string("2", PRIMARY_COLOR)
        + colored_string("-", SECONDARY_COLOR)
        + colored_string(" Drop course from waiting list\n", TEXT_COLOR)
        + colored_string("3", PRIMARY_COLOR)
        + colored_string("-", SECONDARY_COLOR)
        + colored_string(" List available courses\n", TEXT_COLOR)
        + colored_string("4", PRIMARY_COLOR)
        + colored_string("-", SECONDARY_COLOR)
        + colored_string(" List waiting courses\n", TEXT_COLOR)
        + colored_string("5", PRIMARY_COLOR)
        + colored_string("-", SECONDARY_COLOR)
        + colored_string(" List approved courses\n", TEXT_COLOR)
        + colored_string("6", PRIMARY_COLOR)
        + colored_string("-", SECONDARY_COLOR)
        + colored_string(" List rejected courses\n", TEXT_COLOR)
        + colored_string("7", PRIMARY_COLOR)
        + colored_string("-", SECONDARY_COLOR)
        + colored_string(" List transcript\n", TEXT_COLOR)
        + colored_string("8", PRIMARY_COLOR)
        + colored_string("-", SECONDARY_COLOR)
        + colored_string(" Exit\n", EXIT_COLOR)
        + colored_string("Please select an option: ", INPUT_COLOR)
    )


print(getMenu())