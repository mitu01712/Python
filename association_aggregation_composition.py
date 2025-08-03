# Association, Aggregation, Composition
#Student, Laptop
# Association example:
class Laptop:
    def __init__(self, brand):
        self.brand = brand

class Student:
    def __init__(self, name,laptop_obj):
        self.name = name
        self.laptop_v = laptop_obj
    
    def show_laptop_info(self):
        print(f"{self.name} has a laptop named {self.laptop_v.brand}")

lp1 = Laptop("ASUS")
student = Student("Rahim", lp1)
student.show_laptop_info()

# Aggregation (combination of multiple objects) eta holo has a relationship
# example: University has departments

class Department:
    def __init__(self, name):
        self.name = name

class University:
    def __init__(self, name):
        self.name = name
        self.departments = []
    def add_department(self, department):
        self.departments.append(department)
    
    def show_department(self):
        return [department.name for department in self.departments]

un1 = University("ABC University")
dep1 = Department("Proramming")
dep2 = Department("Math")
dep3 = Department("BBA")
dep4 = Department("English")
dep5 = Department("Bangla")
un1.add_department(dep1)
un1.add_department(dep2)
un1.add_department(dep3)
un1.add_department(dep4)
un1.add_department(dep5)

un1.show_department()
print(un1.show_department())



"""return [department.name for department in self.departments]
এখানে List Comprehension ব্যবহার করা হয়েছে।
আমি এটা একদম সহজভাবে, ভেঙে ভেঙে বুঝিয়ে দিচ্ছি যেন মাথায় গেঁথে যায়। 😎

🔍 ধরো এইভাবে ডাটা আছে:
self.departments = [dep1, dep2, dep3]
এবং এই dep1, dep2, dep3 হল Department class-এর object।
প্রতিটার মধ্যে আছে .name নামে property।

🔽 Example:

Object	name
dep1	"Programming"
dep2	"Math"
dep3	"BBA"

এখন এই লাইনটা কী করছে?
[department.name for department in self.departments]
এইটা হচ্ছে list comprehension:

👉 এটি মানে:
“self.departments এর প্রতিটা department object থেকে department.name নিয়ে একটা নতুন list তৈরি করো।”
"""

#Strong relationship
#Composition (eka oporke chara thakte pare na)
#car , engine

class Engine:
    def __init__(self, power):
        self.power = power
    
class Car:
    def __init__(self,brand,power ):
        self.brand = brand
        self.engine = Engine(power)# ekta car bananor sathe sathe engine assigne hoye jabe
        # bisoy ta emon car exised na korle engine o exised korbe na

    def show_details(self):
        print(f"{self.brand} has an engine with {self.engine.power} HP")

car = Car("Toyota", 100)
car.show_details()
"""
🔗 1. Association (সম্পর্ক)
🧠 ব্যাখ্যা:
দুইটা ক্লাস আলাদা, কিন্তু একে অপরকে চেনে।
তারা আলাদা থাকলেও সমস্যা নেই।

🎓 উদাহরণ:
একজন শিক্ষক একজন ছাত্রকে পড়ান।
তবে শিক্ষক বা ছাত্র আলাদাভাবে টিকে থাকতে পারে।

✅ কোড:
class Teacher:
    def __init__(self, name):
        self.name = name

class Student:
    def __init__(self, name):
        self.name = name

# Association: শুধু পরিচয়
teacher1 = Teacher("Mr. Rahim")
student1 = Student("Karim")

print(f"{teacher1.name} teaches {student1.name}")
"""



#Aggregation
"""
⚪ 2. Aggregation (জোড়া লাগানো সম্পর্ক)
🧠 ব্যাখ্যা:
একটা বড় জিনিস ছোট জিনিসগুলোকে ধরে রাখে,
কিন্তু ছোট জিনিসটা আলাদাভাবে বেঁচে থাকতে পারে।

🎓 উদাহরণ:
একটা বিশ্ববিদ্যালয়ে ছাত্র আছে।
তবে ছাত্র সেই বিশ্ববিদ্যালয় ছাড়া অন্য জায়গাতেও থাকতে পারে।

✅ কোড:
class Student:
    def __init__(self, name):
        self.name = name

class University:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

# Student আগে থেকেই আছে
student1 = Student("Karim")

# University student কে গ্রহণ করছে (Aggregation)
university1 = University("Dhaka University")
university1.add_student(student1)

print(f"{student1.name} studies at {university1.name}")
"""

"""
🟣 3. Composition (সম্পূর্ণ নির্ভর সম্পর্ক)
🧠 ব্যাখ্যা:
ছোট জিনিসটা parent object ছাড়া টিকে থাকতে পারে না।
একটা object মারা গেলে এর ভেতরের object গুলোও মারা যায়।

🎓 উদাহরণ:
একটা বাড়ির ভেতরে Bedroom ও Kitchen থাকে।
বাড়ি না থাকলে ঘরগুলোও থাকবে না।

✅ কোড:   
class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self):
        # এখানে House নিজেই Room তৈরি করে (Composition)
        self.bedroom = Room("Bedroom")
        self.kitchen = Room("Kitchen")

house1 = House()
print(f"The house has a {house1.bedroom.name} and a {house1.kitchen.name}")
👉 এখানে Room গুলো House এর সঙ্গে তৈরি হয়েছে। House না থাকলে Room গুলো থাকবে না।
"""