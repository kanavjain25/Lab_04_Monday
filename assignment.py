class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

def sort_employees(employees, sorting_parameter):
    if sorting_parameter == 1:
        return sorted(employees, key=lambda emp: emp.age)
    elif sorting_parameter == 2:
        return sorted(employees, key=lambda emp: emp.name)
    elif sorting_parameter == 3:
        return sorted(employees, key=lambda emp: emp.salary)
    else:
        raise ValueError("Invalid sorting parameter")

if __name__ == "__main__":
    employees_data = [
        ("161E90", "Raman", 41, 56000),
        ("161F91", "Himadri", 38, 67500),
        ("161F99", "Jaya", 51, 82100),
        ("171E20", "Tejas", 30, 55000),
        ("171G30", "Ajay", 45, 44000),
    ]

    employees = [Employee(emp_id, name, age, salary) for emp_id, name, age, salary in employees_data]

    print("Choose sorting parameter:")
    print("1. Sort by Age")
    print("2. Sort by Name")
    print("3. Sort by Salary")

    try:
        sorting_parameter = int(input("Enter your choice: "))
        sorted_employees = sort_employees(employees, sorting_parameter)
        
        print("\nSorted Employee List:")
        for employee in sorted_employees:
            print(employee)
    except ValueError:
        print("Invalid choice. Please enter a valid sorting parameter (1, 2, or 3).")
