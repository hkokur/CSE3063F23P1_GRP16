import json
import os

from Student import Student
from Course import Course
from Lecturer import Lecturer
from Advisor import Advisor
from MandatoryCourse import MandatoryCourse
from TechnicalElectiveCourse import TechnicalElectiveCourse
from NonTechnicalElectiveCourse import NonTechnicalElectiveCourse


class DataUtils:
    def __init__(self):
        self.students = []
        self.courses = []
        self.lecturers = []
        self.advisors = []
        self.mandatories = []
        self.technical_electives = []
        self.non_technical_electives = []

    def save(self):
        self.write_students()
        self.write_courses()
        self.write_lecturers()
        self.write_advisors()
        self.write_mandatory_courses()
        self.write_technical_elective_courses()
        self.write_non_technical_elective_courses()

    @staticmethod
    def get_instance():
        if not hasattr(DataUtils, "_instance"):
            DataUtils._instance = DataUtils()
        return DataUtils._instance

    @staticmethod
    def update_value(key_path, update_text, json_text):
        keys = key_path.split("/")
        data = json.loads(json_text)
        for key in keys[:-1]:
            data = data[key]

        final_key = keys[-1]
        data[final_key] = json.loads(update_text)

        return json.dumps(data)

    @staticmethod
    def write_pretty(file_path):
        with open(file_path, 'r+') as file:
            content = file.read()
            data = json.loads(content)
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)

    def get_student_files(self, folder):
        files = []
        for file_name in os.listdir(folder):
            if file_name.startswith("15"):
                files.append(os.path.join(folder, file_name))
        return files

    def get_parameters_file(self, folder):
        for file_name in os.listdir(folder):
            if file_name.startswith("para"):
                return os.path.join(folder, file_name)
        return None

    def read_students(self):
        student_files = self.get_student_files("python_iteration/database")
        students = []
        for file_path in student_files:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                student = Student.from_json(content)
                students.append(student)
        return students

    def write_students(self):
        student_files = self.get_student_files("python_iteration/database")
        for file_path in student_files:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                json_object = json.loads(content)
                for student in self.students:
                    if student.password == json_object["password"]:
                        updated_string = json.dumps(student.__dict__, indent=4, default=lambda o: o.__dict__)
                        with open(file_path, 'w', encoding='utf-8') as writer:
                            writer.write(updated_string)
                            break

    def read_courses(self):
        parameters_file = self.get_parameters_file("python_iteration/database")
        courses = []
        with open(parameters_file, 'r', encoding='utf-8') as file:
            content = file.read()
            json_object = json.loads(content)
            for course_json in json_object["courses"]:
                course = Course.from_json(course_json)
                courses.append(course)
        return courses

    def write_courses(self):
        parameters_file = self.get_parameters_file("python_iteration/database")
        with open(parameters_file, 'r', encoding='utf-8') as file:
            content = file.read()
            s_courses = [course.to_json() for course in self.courses]
            updated_string = self.update_value("courses", json.dumps(s_courses), content)
            with open(parameters_file, 'w', encoding='utf-8') as writer:
                writer.write(updated_string)
        self.write_pretty(parameters_file)

    def read_lecturers(self):
        parameters_file = self.get_parameters_file("python_iteration/database")
        lecturers = []
        with open(parameters_file, 'r', encoding='utf-8') as file:
            content = file.read()
            json_object = json.loads(content)
            for lecturer_json in json_object["lecturers"]:
                lecturer = Lecturer.from_json(lecturer_json)
                lecturers.append(lecturer)
        return lecturers

    def write_lecturers(self):
        parameters_file = self.get_parameters_file("python_iteration/database")
        with open(parameters_file, 'r', encoding='utf-8') as file:
            content = file.read()
            s_lecturers = [lecturer.to_json() for lecturer in self.lecturers]
            updated_string = self.update_value("lecturers", json.dumps(s_lecturers), content)
            with open(parameters_file, 'w', encoding='utf-8') as writer:
                writer.write(updated_string)
        self.write_pretty(parameters_file)

    def read_advisors(self):
        parameters_file = self.get_parameters_file("python_iteration/database")
        advisors = []
        with open(parameters_file, 'r', encoding='utf-8') as file:
            content = file.read()
            json_object = json.loads(content)
            for advisor_json in json_object["advisors"]:
                advisor = Advisor.from_json(advisor_json)
                advisors.append(advisor)
        return advisors

    def write_advisors(self):
        parameters_file = self.get_parameters_file("python_iteration/database")
        with open(parameters_file, 'r', encoding='utf-8') as file:
            content = file.read()
            s_advisors = [advisor.to_json() for advisor in self.advisors]
            updated_string = self.update_value("advisors", json.dumps(s_advisors), content)
            with open(parameters_file, 'w', encoding='utf-8') as writer:
                writer.write(updated_string)
        self.write_pretty(parameters_file)

    def read_mandatory_courses(self):
        parameters_file = self.get_parameters_file("python_iteration/database")
        mandatories = []
        with open(parameters_file, 'r', encoding='utf-8') as file:
            content = file.read()
            json_object = json.loads(content)
            for mandatory_json in json_object["mandatories"]:
                mandatory = MandatoryCourse.from_json(mandatory_json)
                mandatories.append(mandatory)
        return mandatories

    def write_mandatory_courses(self):
        parameters_file = self.get_parameters_file("python_iteration/database")
        with open(parameters_file, 'r', encoding='utf-8') as file:
            content = file.read()
            s_mandatories = [mandatory.to_json() for mandatory in self.mandatories]
            updated_string = self.update_value("mandatories", json.dumps(s_mandatories), content)
            with open(parameters_file, 'w', encoding='utf-8') as writer:
                writer.write(updated_string)
        self.write_pretty(parameters_file)

    def read_technical_elective_courses(self):
        parameters_file = self.get_parameters_file("python_iteration/database")
        technical_electives = []
        with open(parameters_file, 'r', encoding='utf-8') as file:
            content = file.read()
            json_object = json.loads(content)
            for technical_elective_json in json_object["technicalElectives"]:
                technical_elective = TechnicalElectiveCourse.from_json(technical_elective_json)
                technical_electives.append(technical_elective)
        return technical_electives

    def write_technical_elective_courses(self):
        parameters_file = self.get_parameters_file("python_iteration/database")
        with open(parameters_file, 'r', encoding='utf-8') as file:
            content = file.read()
            s_technical_electives = [course.to_json() for course in self.technical_electives]
            updated_string = self.update_value("technicalElectives", json.dumps(s_technical_electives), content)
            with open(parameters_file, 'w', encoding='utf-8') as writer:
                writer.write(updated_string)
        self.write_pretty(parameters_file)

    def read_non_technical_elective_courses(self):
        parameters_file = self.get_parameters_file("python_iteration/database")
        non_technical_electives = []
        with open(parameters_file, 'r', encoding='utf-8') as file:
            content = file.read()
            json_object = json.loads(content)
            for non_technical_elective_json in json_object["nonTechnicalElectives"]:
                non_technical_elective = NonTechnicalElectiveCourse.from_json(non_technical_elective_json)
                non_technical_electives.append(non_technical_elective)
        return non_technical_electives

    def write_non_technical_elective_courses(self):
        parameters_file = self.get_parameters_file("python_iteration/database")
        with open(parameters_file, 'r', encoding='utf-8') as file:
            content = file.read()
            s_non_technical_electives = [course.to_json() for course in self.non_technical_electives]
            updated_string = self.update_value("nonTechnicalElectives", json.dumps(s_non_technical_electives), content)
            with open(parameters_file, 'w', encoding='utf-8') as writer:
                writer.write(updated_string)
        self.write_pretty(parameters_file)
