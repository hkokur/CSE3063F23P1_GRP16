from models import Course  # Assuming Course class is in a separate file
from models import TimeInterval  # Assuming TimeInterval class is in a separate file
from interfaces import SectionInterface  # Assuming SectionInterface class is in a separate file
from models import Lecturer  # Assuming Lecturer class is in a separate file

class TechnicalElectiveCourse(Course, SectionInterface):
    def __init__(self, course, dates, section_name, lecturer, quota, location, required_credit=None):
        super().__init__(course.short_name, course.full_name, course.description, course.prerequisite,
                         course.semester, course.credit, course.class_hours)
        self.dates = dates
        self.section_name = section_name
        self.lecturer = lecturer
        self.quota = quota
        self.location = location
        self.required_credit = required_credit

    # Interface Methods
    def is_technical(self):
        return True

    def is_mandatory(self):
        return False

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

    # Abstract Methods
    def __str__(self):
        return f"Technical Elective Course: {self.get_full_name()}\nCode: {self.get_short_name()}\nDescription: {self.get_description()}\n" \
               f"Prerequisite: {self.get_prerequisites()}\nSemester: {self.get_semester()}\nCredit: {self.get_credit()}\n" \
               f"Class Hours: {self.get_class_hours()}\nSection Name: {self.get_section_name()}\nLecturer: {self.get_lecturer().get_full_name()}\n" \
               f"Quota: {self.get_quota()}\nLocation: {self.location}\nRequiredCredit: {self.required_credit}\n-------------"

    # Class Methods
    def get_required_credit(self):
        return self.required_credit

    def set_required_credit(self, required_credit):
        self.required_credit = required_credit

    def check_required_credit(self, total_credit):
        return total_credit >= self.required_credit
