from models import Course, TimeInterval
from models import Lecturer
from interfaces import SectionInterface


class MandatoryCourse(Course, SectionInterface):
    def __init__(self, course, dates, section_name, lecturer, quota, location, lab_hours):
        super().__init__(course.get_short_name(), course.get_full_name(), course.get_description(),
                         course.get_prerequisite(), course.get_semester(), course.get_credit(),
                         course.get_class_hours())
        self.dates = dates
        self.section_name = section_name
        self.lecturer = lecturer
        self.quota = quota
        self.location = location
        self.lab_hours = lab_hours

    def __init__(self, short_name, full_name, description, prerequisite, semester, credit, class_hours,
                 dates, section_name, lecturer, quota, location, lab_hours):
        super().__init__(short_name, full_name, description, prerequisite, semester, credit, class_hours)
        self.dates = dates
        self.section_name = section_name
        self.lecturer = lecturer
        self.quota = quota
        self.location = location
        self.lab_hours = lab_hours

    # Interface Methods
    def is_technical(self):
        return False

    def is_mandatory(self):
        return True

    def set_dates(self, dates):
        self.dates = dates

    def get_dates(self):
        return self.dates

    def add_date(self, date):
        self.dates.append(date)
        return True

    def remove_date(self, date):
        self.dates.remove(date)
        return True

    def get_section_name(self):
        return self.section_name

    def set_section_name(self, section_name):
        self.section_name = section_name

    def get_lecturer(self):
        return self.lecturer

    def set_lecturer(self, lecturer):
        self.lecturer = lecturer

    def get_quota(self):
        return self.quota

    def set_quota(self, quota):
        self.quota = quota

    # Class Methods
    def __str__(self):
        return f"Mandatory Course: {self.get_full_name()}\nCode: {self.get_short_name()}\nDescription: {self.get_description()}\n" \
               f"Prerequisite: {self.get_prerequisites()}\nSemester: {self.get_semester()}\nCredit: {self.get_credit()}\n" \
               f"Class Hours: {self.get_class_hours()}\nSection Name: {self.get_section_name()}\nLecturer: {self.get_lecturer().get_full_name()}\n" \
               f"Quota: {self.get_quota()}\nLocation: {self.location}\nLab Hours: {self.lab_hours}\n------------"

    def has_labs(self):
        return self.lab_hours > 0
