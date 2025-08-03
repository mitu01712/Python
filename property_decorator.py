# Property Decorator

class Employee:
    company_name = "Ostad Company"
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property 
    def salary(self):
        return self._salary
    # keu jeno chailei set korte na pare
    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary
    
ob1 = Employee("Ramin", 40000)
print(ob1.salary)# @property use korar karon e amra get_salary() method ke variable hisebe use korte parbo

ob1.salary =7000
print(ob1.salary)






"""
✅ ধরি তুমি একটা class বানালে – Student
class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks
এখানে তুমি চাও কেউ সরাসরি _marks এর ভ্যালু না নেয় বা চেঞ্জ না করে।

তখন তুমি getter ও setter method বানিয়ে রাখো:

    def get_marks(self):
        return self._marks

    def set_marks(self, value):
        if value >= 0 and value <= 100:
            self._marks = value
        else:
            print("Marks must be between 0 and 100")
🔹 ব্যবহার করতে হলে লিখতে হয়:

s1 = Student("Mitu", 90)

print(s1.get_marks())       # getter
s1.set_marks(95)            # setter
এভাবে ফাংশন ডেকে ডেকে কাজ করতে হচ্ছে। বারবার () দিতে হচ্ছে। এটা ঝামেলা।

🪄 এখন আসল Magic – @property
Python বলে,

"তুমি চাইলে function-কেও variable এর মতো ব্যবহার করতে পারো!"

এই কাজটা করার জন্যই আমরা @property ব্যবহার করি।

✅ @property দিয়ে Rewrite করি

class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:   # এর মানে:value ≥ 0 এবং value ≤ 100
            self._marks = value
        else:
            print("Marks must be between 0 and 100")
🔹 এখন আর get_marks() বা set_marks() call করতে হবে না
s1 = Student("Mitu", 90)

print(s1.marks)       # getter এর মতো, কিন্তু () নেই
s1.marks = 95         # setter এর মতো, কিন্তু () নেই
🧠 সহজ করে মনে রাখো:
যেটা আগে ছিলো	এখন যেটা হবে	কারণ
s1.get_marks()	s1.marks	@property
s1.set_marks(95)	s1.marks = 95	@marks.setter

🔄 তাহলে @property এর কাজ কী?
🔹 ফাংশনকে এমন বানায় যেন মনে হয় এটা ভ্যারিয়েবল
🔹 ভ্যালু পড়া ও চেঞ্জ করার জন্য ভিন্ন ভিন্ন ফাংশন দরকার হয় না
🔹 কোড ছোট, পরিষ্কার, সুন্দর হয়

✅ একটা ছোট গল্প দিয়ে মনে রাখো:
তুমি s1.marks = 1000 লিখলে, Python কিন্তু সরাসরি _marks চেঞ্জ করবে না।
Python বলবে:

"এই ভ্যারিয়েবল @property দেওয়া, মানে আমি আগে চেক করবো – ১০০০ valid কিনা। Valid হলে তবেই সেট করবো।"

এটা হচ্ছে @property-এর আসল মজা!

📌 মনে রাখার কৌশল:
@property      ➜ value পড়ার জন্য (getter)
@var.setter ➜ value সেট করার জন্য (setter) # je variable ta ke protected vabe rakhte chai setar nam.setter
"""