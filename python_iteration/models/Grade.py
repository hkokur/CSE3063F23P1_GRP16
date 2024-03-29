from Course import Course


class Grade:
    def __init__(self, course=None, grade=None):
        self.__course = course
        self.__grade = grade

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade):
        self.__grade = grade

    def get_credit(self):
        return self.__course.credit

    def setcourse(self, course) -> bool:
        if isinstance(course, Course):
            self.__course = course
        else:
            raise ValueError(
                "Invalid course object. Must be an instance of Course class."
            )
        return True

    def get_course_short_name(self) -> str:
        return self.__course.short_name

    def get_course_full_name(self) -> str:
        return self.__course.full_name

    def __eq__(self, other):
        return self.get_course_short_name() == other.get_course_short_name()
