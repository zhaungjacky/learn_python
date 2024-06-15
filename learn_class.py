import datetime
from typing import List


#  python OOP
class Employee:

    num_of_emps: int = 0
    raise_amount: float = 1.04

    def __init__(
        self,
        fname: str,
        lname: str,
        hobby: list[str] = None,
        salary: float = 3000.0,
    ) -> None:
        self.fname = fname
        self.lname = lname
        self.hobby = hobby
        self.salary = salary
        self.info = f"{self.fname} earn {self.salary} now!"
        Employee.num_of_emps += 1

    @property
    def email(self) -> str:
        return f"{self.fname.lower()}.{self.lname.lower()}@company.com"


    # regular method
    @property
    def fullname(self) -> str:
        return f"{self.fname} {self.lname}"
    
    @fullname.setter
    def fullname(self,new_name: str):
        fname,lname = new_name.split(" ")
        self.fname = fname
        self.lname = lname

    @fullname.deleter
    def fullname(self):
        print("delete name")
        self.fname = None
        self.lname = None
        # self.fname = None
        # self.fname = None



    def apply_raise(self):
        self.salary = float(self.salary * self.raise_amount)
        # self.salary = int(self.salary * Employee.apply_raise)

    
    def __repr__(self) -> str: #  for debug
        return f"Employee('{self.fname}','{self.lname}',{self.hobby},{self.salary})"

    def __str__(self) -> str:
        return f"{self.fullname()} - {self.info}"
    
    def __add__(self, other_emp): 
        return self.salary + other_emp.salary
    
    def __len__(self):
        return len(self.fullname())
        
    
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str: str):
        fname, lname, salary = emp_str.split("-")
        return cls(
            fname=fname,
            lname=lname,
            hobby=None,
            salary=salary,
        )

    @staticmethod
    def is_workday(day: datetime.date) -> bool:
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee("Corey","Schafer",["python"],9800.0)
emp_2 = Employee("Jacky","Nelson",["dart"],8800.0)

# print(emp_1.info)
# print(emp_1.email)
# emp_1.fname = "Jone"

emp_1.fullname = "Shining Zhaung"
print(emp_1.info)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
# print(emp_1.info)
# print(emp_1.email)
# print(emp_1.fullname)

# add_salary = emp_1.__add__(emp_2)
# print(add_salary)
# print(emp_1 + emp_2)
# print(len(emp_1))
# emp_2 = Employee('Corey','Schafer',['python'],9800.0)
# print(emp_1)
# print(repr(emp_1))
# print(str(emp_1))
# print(emp_1.__repr__())
# print(emp_1.__str__())

# print(1 +2)
# print(int.__add__(1,2))

class Developer(Employee):

    raise_amount: float = 1.1

    def __init__(
        self,
        fname: str,
        lname: str,
        prog_lang: str,
        hobby: List[str] = None,
        salary: float = 6000.0,
    ) -> None:
        super().__init__(fname, lname, hobby, salary,)
        self.prog_lang = prog_lang
        self.email = f"{fname.lower()}.{lname.lower()}@gmail.com"

class Manager(Employee):

    def __init__(
        self,
        fname: str,
        lname: str,
        employees: List[Developer] = None,
        hobby: List[str] = None,
        salary: float = 7000.0,
    ) -> None:
        super().__init__(fname, lname, hobby, salary)
        if employees is None:
            self.employees= []
        else:
            self.employees = employees

    def add_emp(self, new_emp: Developer):
        if new_emp not in self.employees:
            self.employees.append(new_emp)
    def remove_emp(self, emp: Developer):
        if emp  in self.employees:
            self.employees.remove(emp)

    def prinf_emps(self):
        for emp in self.employees:
            print(f"-->{emp.fullname()}")


# dev_1 = Developer(
#     fname="Corey",
#     lname="Schafer",
#     prog_lang="python"
# )
# dev_2 = Developer(
#     fname="test",
#     lname="Employee",
#     prog_lang="dart",
#     salary=8800
# )

# manger_1 = Manager(fname="Alex",lname="Collison",hobby=["money","manager"],salary=7777,employees=[dev_1])


# print(isinstance(manger_1,Developer))
# print(isinstance(dev_1,Manager))
# print(isinstance(dev_2,Employee))

# print(issubclass(Manager,Employee))
# print(issubclass(Manager,Developer))

# manger_1.add_emp(dev_1)
# manger_1.add_emp(dev_2)
# manger_1.prinf_emps()
# manger_1.add_emp(dev_2)
# manger_1.prinf_emps()
# manger_1.remove_emp(dev_1)
# manger_1.prinf_emps()

# print(dev_1.prog_lang)
# print(dev_2.prog_lang)

# print(dev_1.salary)
# dev_1.apply_raise()
# print(dev_1.salary)

# print(help(Developer))

# print(dev_2.info)
# print(dev_2.email)

# emp_1 = Employee(
#     fname="Jacky",
#     lname="Zhaung",
#     hobby=[
#         "dota2",
#         "coding",
#     ],
#     salary=5000,
# )
# emp_2 = Employee(
#     fname="Corey",
#     lname="Schafer",
#     hobby=[
#         "dota2",
#         "coding",
#     ],
#     salary=5150,
# )

# print(Employee.is_workday(datetime.date(2024, 6, 8)))

# emp_str_1 = "John-Doe-7000"
# emp_str_2 = "Steve-Smith-8000"
# emp_str_3 = "Mike-Jordon-9000"
# new_emp_1 = Employee.from_string(emp_str_1)
# new_emp_2 = Employee.from_string(emp_str_2)
# new_emp_3 = Employee.from_string(emp_str_3)

# print(new_emp_1.info)
# print(new_emp_2.info)
# print(new_emp_3.info)


# Employee.set_raise_amount(1.08)
# emp_1.raise_amount = 1.06

# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)

# emp_1.raise_amount = 1.06

# print(emp_1.__dict__)
# print(emp_2.__dict__)

# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)

# print(Employee.num_of_emps)

# print(emp_1.__dict__)
# print("___________________")
# print(Employee.__dict__)
# print(emp_1)
# print(emp_2)

# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)


# me.salary(5851)
# me.fullname()
# print(Employee.fullname(emp_1))

# full_name = me.fullname()
# print(me.salary)
# print(me.info)
# print(full_name)
# for hobby in me.hobby:
#     print(hobby)
