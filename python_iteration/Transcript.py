class Transcript:
    def __init__(self, initial_grades=None, notes=""):
        self.list_grades = [] if initial_grades is None else initial_grades.copy()
        self.notes = notes

    def get_grades(self):
        result = ""
        for grade in self.list_grades:
            result += f"Course name: {grade.course.full_name} | Student Grade: {grade.grade}\n"
        return result

    def get_grade_list(self):
        return self.list_grades

    def add_grade(self, grade):
        self.list_grades.append(grade)
        return grade is None

    def delete_grade(self, grade):
        for i in range(len(self.list_grades)):
            if self.list_grades[i] == grade:
                del self.list_grades[i]
                return True
        return False

    def calculate_cumulative_gpa(self):
        total_credit = 0
        sum_product = 0

        for grade in self.list_grades:
            credit = grade.course.credit
            total_credit += credit
            sum_product += float(grade.grade) * credit

        if total_credit == 0:
            return 0.0

        return sum_product / total_credit

    def calculate_semester_gpa(self, semester):
        total_credit = 0
        sum_product = 0

        for grade in self.list_grades:
            if grade.course.semester == semester:
                credit = grade.course.credit
                total_credit += credit
                sum_product += float(grade.grade) * credit

        if total_credit == 0:
            return 0.0

        return sum_product / total_credit

    def get_notes(self):
        return self.notes

    def set_notes(self, notes):
        self.notes = notes

    def __str__(self):
        result = f"Transcript: \nGrades: \n{self.get_grades()}Notes: {self.notes}\n"
        return result
