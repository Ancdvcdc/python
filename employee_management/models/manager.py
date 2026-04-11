from .employee import Employee

class Manager(Employee):
    def calculate_salary(self):
        return self.salary * 2