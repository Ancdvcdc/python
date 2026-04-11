from exceptions.employee_exceptions import *

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        for e in self.employees:
            if e.emp_id == emp.emp_id:
                raise DuplicateEmployeeError("Trùng ID")
        self.employees.append(emp)

    def find_employee(self, emp_id):
        for e in self.employees:
            if e.emp_id == emp_id:
                return e
        raise EmployeeNotFoundError(emp_id)

    def delete_employee(self, emp_id):
        emp = self.find_employee(emp_id)
        self.employees.remove(emp)

    def list_employees(self):
        if not self.employees:
            raise IndexError("Chưa có dữ liệu")
        return self.employees