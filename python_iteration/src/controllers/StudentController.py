import logging
from models import Course, Student, Transcript

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class StudentController:
    def __init__(self, student=None):
        self.student = student

    # Adds the course to the selected courses of the student.
    def add_course(self, course: Course):
        try:
            self.student.add_course(course)
            logger.info(f"Course added: {course.get_short_name()} to student: {self.student.get_person_name()}")
        except Exception as e:
            logger.error(f"Error occurred while adding course: {course.get_short_name()} to student: {self.student.get_person_name()}")

    # Drops the course from the selected courses of the student.
    def drop_course(self, course: Course):
        try:
            self.student.drop_course(course)
            logger.info(f"Course dropped: {course.get_short_name()} from student: {self.student.get_person_name()}")
        except Exception as e:
            logger.error(f"Error occurred while dropping course: {course.get_short_name()} from student: {self.student.get_person_name()}")

    # Returns the available courses for the student.
    def get_available_courses(self):
        try:
            return self.student.get_available_courses()
        except Exception as e:
            logger.error(f"Error occurred while getting available courses for student: {self.student.get_person_name()}")
            return None

    # Returns the selected courses of the student.
    def get_selected_courses(self):
        try:
            return self.student.get_selected_courses()
        except Exception as e:
            logger.error(f"Error occurred while getting selected courses for student: {self.student.get_person_name()}")
            return None

    # Returns person name of the student.
    def get_person_name(self):
        try:
            return self.student.get_person_name()
        except Exception as e:
            logger.error(f"Error occurred while getting person name for student: {self.student.get_person_name()}")
            return None

    # Returns person surname of the student.
    def get_person_surname(self):
        try:
            return self.student.get_person_surname()
        except Exception as e:
            logger.error(f"Error occurred while getting person surname for student: {self.student.get_person_name()}")
            return None

    # Returns the student's transcript.
    def get_transcript(self):
        try:
            return self.student.get_transcript()
        except Exception as e:
            logger.error(f"Error occurred while getting transcript for student: {self.student.get_person_name()}")
            return None

    def get_status(self):
        try:
            return self.student.get_status()
        except Exception as e:
            logger.error(f"Error occurred while getting status for student: {self.student.get_person_name()}")
            return None

    # Sends approval request to the advisor.
    def send_approval_request(self):
        try:
            logger.info(f"Approval request sent to advisor for student: {self.student.get_person_name()}")
            return self.student.send_approval_request()
        except Exception as e:
            logger.error(f"Error occurred while sending approval request to advisor for student: {self.student.get_person_name()}")
            return False

    def get_warnings(self):
        try:
            return self.student.get_warnings()
        except Exception as e:
            logger.error(f"Error occurred while getting warnings for student: {self.student.get_person_name()}")
            return None
