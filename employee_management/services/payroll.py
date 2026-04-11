def total_salary(employees):
    return sum(e.calculate_salary() for e in employees)