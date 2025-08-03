# Class VS Instance Method

class Employee:
    company_name = "Ostad Company"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display_info(self):
        print(f"Employee Name:{self.name}\n Salary :{self.salary}")
    @classmethod
    def change_company_name(cls, name):
        cls.company_name = name
ob1 = Employee("Mitu", 30000)
ob2 = Employee("satu", 30000)
ob1.display_info()
ob2.display_info()
Employee.change_company_name("ABC Company")
print(ob1.company_name)
print(ob2.company_name)

# common part rakhar jonno amra class method or calss variable  ke use kori
# qunic part rakhar jonno amra intence variable or instance method use kori

"""
class Employee:
    company_name = "Ostad Company"  # 👉 এটি একটি class variable
    
    def __init__(self, name, salary):
        self.name = name            # 👉 instance variable
        self.salary = salary        # 👉 instance variable
    
    def display_info(self):
        print(f"Employee Name:{self.name}\n Salary :{self.salary}")  # 👉 instance info display
    
    @classmethod
    def change_company_name(cls, name):
        cls.company_name = name     # 👉 class variable update করার method

ob1 = Employee("Mitu", 30000)       # 👉 একটি object তৈরি করলাম
ob2 = Employee("satu", 30000)      # 👉 আরেকটি object

ob1.display_info()                 # ob1 er information print korbe
ob2.display_info()                # 👉 শুধু ob2 এর তথ্য প্রিন্ট করছি
Employee.change_company_name("ABC Company")  # 👉 class variable পরিবর্তন করছি

print(ob1.company_name)           # 👉 ob1 এর company_name প্রিন্ট করব
print(ob2.company_name)           # 👉 ob2 এর company_name প্রিন্ট করব

"""