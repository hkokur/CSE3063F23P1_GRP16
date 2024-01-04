class Person:
    def __init__(self, person_name, person_surname, username, password):
        self.person_name = person_name
        self.person_surname = person_surname
        self.username = username
        self.password = password

    def __init__(self):
        pass

    def get_person_name(self):
        return self.person_name

    def get_full_name(self):
        return f"{self.person_name} {self.person_surname}"

    def set_person_name(self, person_name):
        self.person_name = person_name

    def get_person_surname(self):
        return self.person_surname

    def set_person_surname(self, person_surname):
        self.person_surname = person_surname

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password
