class Employee:
    def __init__(self, emp_name: str, emp_id: str, emp_salary: int, emp_department: str):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    
    def calculate_emp_salary(self, salary: int, hours_worked: int):
        overtime = 0
        if hours_worked > 50:
            overtime = hours_worked - 50
        
        self.emp_salary = self.emp_salary + overtime * (self.emp_salary / 50)

        
    def emp_assign_department(self, new_department):
        self.emp_department = new_department
    
    def print_employee_details(self):
        print("\nName: ", self.emp_name)
        print("ID: ", self.emp_id)
        print("Salary: ", self.emp_salary)
        print("Department: ", self.emp_department)


employee1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
employee2 = Employee("JONES", "E7499", 45000, "RESEARCH")
employee3 = Employee("MARTIN", "E7900", 50000, "SALES")
employee4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

print("Original Employee Details:")
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()
employee4.print_employee_details()

# Change the departments of employee1 and employee4
employee1.emp_assign_department("OPERATIONS")
employee4.emp_assign_department("SALES")

# Now calculate the overtime of the employees who are eligible:
employee2.calculate_emp_salary(45000, 52)
employee4.calculate_emp_salary(45000, 60)

print("Updated Employee Details:")
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()
employee4.print_employee_details()