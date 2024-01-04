class Course:
    def __init__(self, short_name, full_name, description, prerequisites, semester, credit, class_hours):
        self.short_name = short_name
        self.full_name = full_name
        self.description = description
        self.prerequisites = prerequisites
        self.semester = semester
        self.credit = credit
        self.class_hours = class_hours

    def get_short_name(self):
        return self.short_name

    def set_short_name(self, short_name):
        self.short_name = short_name

    def get_full_name(self):
        return self.full_name

    def set_full_name(self, full_name):
        self.full_name = full_name

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_prerequisites(self):
        return self.prerequisites

    def set_prerequisites(self, prerequisites):
        self.prerequisites = prerequisites

    def remove_prerequisite(self, prerequisite):
        self.prerequisites.remove(prerequisite)
        return True

    def add_prerequisite(self, prerequisite):
        self.prerequisites.append(prerequisite)
        return True

    def get_semester(self):
        return self.semester

    def set_semester(self, semester):
        self.semester = semester

    def get_credit(self):
        return self.credit

    def set_credit(self, credit):
        if 0 < credit < 10:
            self.credit = credit
        else:
            print("Credit must be between 1 and 9")

    def get_class_hours(self):
        return self.class_hours

    def set_class_hours(self, class_hours):
        if 0 < class_hours < 10:
            self.class_hours = class_hours
        else:
            print("Class hours must be between 1 and 9")

    def get_prerequisites_str(self):
        if not self.prerequisites or len(self.prerequisites) == 0:
            return "There is no prerequisite"
        else:
            return " ".join(self.prerequisites)

    def __str__(self):
        return f"Course Code: {self.short_name}\nCourse Name: {self.full_name}\nDescription: {self.description}\n" \
               f"Prerequisite: {self.get_prerequisites_str()}\nSemester: {self.semester}\nCredit: {self.credit}\n" \
               f"Class Hours: {self.class_hours}\n---------"
