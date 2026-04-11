class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.performance = 0
        self.projects = []

    def get_type(self):
        return "Employee"

    def __str__(self):
        return f"{self.emp_id} - {self.name} - {self.get_type()} - Lương: {self.salary} - Hiệu suất: {self.performance}"


class Manager(Employee):
    def get_type(self):
        return "Manager"


class Developer(Employee):
    def __init__(self, emp_id, name, salary, language):
        super().__init__(emp_id, name, salary)
        self.language = language

    def get_type(self):
        return "Developer"

    def __str__(self):
        return super().__str__() + f" - Ngôn ngữ: {self.language}"


class Intern(Employee):
    def get_type(self):
        return "Intern"

employees = []

def add_employee():
    print("1. Manager | 2. Developer | 3. Intern")
    choice = input("Chọn: ")
    emp_id = input("ID: ")
    name = input("Tên: ")
    salary = float(input("Lương: "))

    if choice == "1":
        employees.append(Manager(emp_id, name, salary))
    elif choice == "2":
        lang = input("Ngôn ngữ: ")
        employees.append(Developer(emp_id, name, salary, lang))
    elif choice == "3":
        employees.append(Intern(emp_id, name, salary))


def show_all():
    for e in employees:
        print(e)


def show_by_type():
    t = input("Nhập loại: ")
    for e in employees:
        if e.get_type().lower() == t.lower():
            print(e)


def show_by_performance():
    for e in sorted(employees, key=lambda x: x.performance, reverse=True):
        print(e)


def search():
    print("1.ID | 2.Tên | 3.Ngôn ngữ")
    c = input("Chọn: ")

    if c == "1":
        x = input("ID: ")
        for e in employees:
            if e.emp_id == x:
                print(e)

    elif c == "2":
        x = input("Tên: ")
        for e in employees:
            if x.lower() in e.name.lower():
                print(e)

    elif c == "3":
        x = input("Ngôn ngữ: ")
        for e in employees:
            if isinstance(e, Developer) and e.language == x:
                print(e)


def salary_menu():
    print("1.Tính từng NV | 2.Tổng | 3.Top 3")
    c = input("Chọn: ")

    if c == "1":
        for e in employees:
            print(e.name, e.salary)

    elif c == "2":
        print("Tổng:", sum(e.salary for e in employees))

    elif c == "3":
        top = sorted(employees, key=lambda x: x.salary, reverse=True)[:3]
        for e in top:
            print(e)


def project_menu():
    print("1.Thêm | 2.Xóa | 3.Xem")
    c = input("Chọn: ")
    emp_id = input("ID: ")

    for e in employees:
        if e.emp_id == emp_id:
            if c == "1":
                p = input("Dự án: ")
                e.projects.append(p)
            elif c == "2":
                p = input("Dự án: ")
                if p in e.projects:
                    e.projects.remove(p)
            elif c == "3":
                print(e.projects)


def performance_menu():
    print("1.Cập nhật | 2.Xuất sắc | 3.Cải thiện")
    c = input("Chọn: ")

    if c == "1":
        emp_id = input("ID: ")
        for e in employees:
            if e.emp_id == emp_id:
                e.performance = float(input("Điểm: "))

    elif c == "2":
        for e in employees:
            if e.performance > 8:
                print(e)

    elif c == "3":
        for e in employees:
            if e.performance < 5:
                print(e)


def hr_menu():
    print("1.Xóa | 2.Tăng lương | 3.Thăng chức")
    c = input("Chọn: ")

    if c == "1":
        emp_id = input("ID: ")
        global employees
        employees = [e for e in employees if e.emp_id != emp_id]

    elif c == "2":
        for e in employees:
            e.salary += 1000

    elif c == "3":
        emp_id = input("ID: ")
        for i, e in enumerate(employees):
            if e.emp_id == emp_id:
                if isinstance(e, Intern):
                    employees[i] = Developer(e.emp_id, e.name, e.salary, "Python")
                elif isinstance(e, Developer):
                    employees[i] = Manager(e.emp_id, e.name, e.salary)


def stats():
    from collections import Counter

    print("Theo loại:")
    print(Counter(e.get_type() for e in employees))

    print("Tổng lương:", sum(e.salary for e in employees))

    if employees:
        avg = sum(len(e.projects) for e in employees) / len(employees)
        print("TB dự án:", avg)

while True:
    print("\n===== MENU =====")
    print("1.Thêm NV")
    print("2.Hiển thị")
    print("3.Tìm kiếm")
    print("4.Lương")
    print("5.Dự án")
    print("6.Hiệu suất")
    print("7.Nhân sự")
    print("8.Thống kê")
    print("9.Thoát")

    ch = input("Chọn: ")

    if ch == "1":
        add_employee()
    elif ch == "2":
        print("a.All b.Type c.Performance")
        sub = input()
        if sub == "a":
            show_all()
        elif sub == "b":
            show_by_type()
        elif sub == "c":
            show_by_performance()
    elif ch == "3":
        search()
    elif ch == "4":
        salary_menu()
    elif ch == "5":
        project_menu()
    elif ch == "6":
        performance_menu()
    elif ch == "7":
        hr_menu()
    elif ch == "8":
        stats()
    elif ch == "9":
        break