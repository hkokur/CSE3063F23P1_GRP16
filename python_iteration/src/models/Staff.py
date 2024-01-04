from models import Person  # Assuming Person class is in a separate file
from models import TimeInterval  # Assuming TimeInterval class is in a separate file

class Staff(Person):
    def __init__(self, person_name, person_surname, username, password, reputation, office_hours, salary, employment_status):
        super().__init__(person_name, person_surname, username, password)
        self.reputation = reputation
        self.office_hours = office_hours
        self.salary = salary
        self.employment_status = employment_status

    def set_office_hours(self, office_hours):
        self.office_hours = office_hours

    def get_reputation(self):
        return self.reputation

    def set_reputation(self, reputation):
        self.reputation = reputation

    def get_office_hours(self):
        return self.office_hours

    def add_office_hours(self, office_hour):
        self.office_hours.append(office_hour)

    def delete_office_hours(self, office_hour):
        self.office_hours.remove(office_hour)

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def get_employment_status(self):
        return self.employment_status

    def set_employment_status(self, employment_status):
        self.employment_status = employment_status
