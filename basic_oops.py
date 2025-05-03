class Employee:
    def __init__(self, emp_id: int, emp_salary: int, emp_designation: str) -> None:
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_designation = emp_designation

    def travel(self, destination: str) -> str:
        return f"Employee {self.emp_id} is travelling to destination {destination}."
    
    @staticmethod
    def random_number() -> int:
        import random
        return random.randint(1, 100)
    
    @classmethod
    def from_string(cls, emp_str: str) -> 'Employee':
        emp_id, emp_salary, emp_designation = emp_str.split(',')
        return cls(int(emp_id), int(emp_salary), emp_designation)
    
    def details(self):
        print(f"Employee ID is {self.emp_id}, salary {self.emp_salary} and designation {self.emp_designation}")
    
sam = Employee(1, 1000, "Software Engineer")
print(sam.emp_id)  # Output: 1
print(sam.emp_salary)  # Output: 1000
print(sam.emp_designation)  # Output: Software Engineer
print(sam.travel("New York"))  # Output: Employee 1 is travelling to destination New York.

print(Employee.random_number())  # Output: Random number between 1 and 100

aman = Employee.from_string("23,500000000,software-enginer")

aman.details()
