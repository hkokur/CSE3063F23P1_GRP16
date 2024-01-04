from Staff import Staff
from Course import Course
from MandatoryCourse import MandatoryCourse
from TechnicalElectiveCourse import TechnicalElectiveCourse
from NonTechnicalElectiveCourse import NonTechnicalElectiveCourse

from SectionInterface import SectionInterface

from DataUtils import DataUtils


class Lecturer(Staff):
    def __init__(self, person_name, person_surname, username, password, reputation, office_hours, salary,
                 employment_status, courses):
        super().__init__(person_name, person_surname, username, password, reputation, office_hours, salary,
                         employment_status)
        self.courses = courses if courses else []

    def init_courses(self):
        json = DataUtils.getInstance()
        courses = []
        courses.extend(json.read_mandatory_courses())
        courses.extend(json.read_technical_elective_courses())
        courses.extend(json.read_non_technical_elective_courses())
        new_courses = []
        for course in courses:
            if isinstance(course, SectionInterface):
                if course.get_lecturer().get_username() == self.get_username():
                    if self.courses:
                        is_exist = any(
                            c.get_short_name() == course.get_short_name() and
                            c.get_section_name() == course.get_section_name() for c in self.courses
                        )
                        if not is_exist:
                            self.courses.append(course)
                    else:
                        new_courses.append(course)
                        self.courses = new_courses

    def get_lectured_courses(self):
        self.init_courses()
        return self.courses

    def add_lectured_courses(self, course):
        if isinstance(course, SectionInterface):
            course.set_lecturer(self)
            json = DataUtils.getInstance()
            if isinstance(course, MandatoryCourse):
                courses = json.read_mandatory_courses()
                courses.append(course)
                json.write_mandatory_courses(courses)
            elif isinstance(course, TechnicalElectiveCourse):
                courses = json.read_technical_elective_courses()
                courses.append(course)
                json.write_technical_elective_courses(courses)
            elif isinstance(course, NonTechnicalElectiveCourse):
                courses = json.read_non_technical_elective_courses()
                courses.append(course)
                json.write_non_technical_elective_courses(courses)
            self.init_courses()
            return True
        return False

    def delete_lectured_courses(self, course):
        json = DataUtils.getInstance()
        courses = []
        courses.extend(json.read_mandatory_courses())
        courses.extend(json.read_technical_elective_courses())
        courses.extend(json.read_non_technical_elective_courses())
        for c in courses:
            if isinstance(c, SectionInterface):
                if c.get_lecturer().get_username() == course.get_lecturer().get_username():
                    if isinstance(course, MandatoryCourse):
                        m_courses = json.read_mandatory_courses()
                        m_courses = [mc for mc in m_courses if
                                     mc.get_short_name() != course.get_short_name() or
                                     mc.get_section_name() != course.get_section_name()]
                        json.write_mandatory_courses(m_courses)
                    elif isinstance(course, TechnicalElectiveCourse):
                        t_courses = json.read_technical_elective_courses()
                        t_courses = [tc for tc in t_courses if
                                     tc.get_short_name() != course.get_short_name() or
                                     tc.get_section_name() != course.get_section_name()]
                        json.write_technical_elective_courses(t_courses)
                    elif isinstance(course, NonTechnicalElectiveCourse):
                        n_courses = json.read_non_technical_elective_courses()
                        n_courses = [nc for nc in n_courses if
                                     nc.get_short_name() != course.get_short_name() or
                                     nc.get_section_name() != course.get_section_name()]
                        json.write_non_technical_elective_courses(n_courses)
                    self.init_courses()
                    return True
        return False

    def view_enrolled_students(self, course):
        json = DataUtils.getInstance()
        students = json.read_students()
        enrolled_students = []
        for student in students:
            selected_courses = student.get_selected_courses()
            for selected_course in selected_courses:
                if selected_course.get_short_name() == course.get_short_name():
                    if isinstance(selected_course, (MandatoryCourse, TechnicalElectiveCourse, NonTechnicalElectiveCourse)):
                        if selected_course.get_lecturer().get_username() == self.get_username():
                            enrolled_students.append(student)
        return enrolled_students
