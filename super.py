class Employee:
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age 
        self.salary = salary

    def display_info(self):
        print(f'Name: {self.name}, Age:{self.age}, Salary: {self.salary}')

class Manager(Employee):
    def __init__(self, name, age, salary, team_size):
        super().__init__(name, age, salary)
        self.team_size = team_size

    def display_info(self):
        super().display_info()
        print(f'Team size: {self.team_size}')

    
class Developer(Employee):
    def __init__(self, name, age, salary, job):
        super().__init__(name, age, salary)
        self.job = job

    def display_info(self):
        super().display_info()
        print(f'Job: {self.job}')   


m = Manager('Azizabek', 25, 100000000, 3)
d = Developer('Ruslan', 14, 10000000, 'Backend Python developer') 


m.display_info()
d.display_info()

        