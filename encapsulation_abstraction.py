# Encapsulation and Abstraction


"""
🔐 1. Encapsulation (এনক্যাপসুলেশন) মানে কী?
Encapsulation মানে হলো
👉 তথ্য (data) আর function (method)-কে একসাথে প্যাকেট করে রাখা
👉 এবং বাইরের দুনিয়া থেকে লুকিয়ে রাখা, যেন কেউ সরাসরি access করতে না পারে।
🔸 মানে, ভিতরের জিনিস বাইরে থেকে পরিবর্তন করা যাবে না সরাসরি।
🔸 এটি data-কে protect করে।
🔸 Python-এ আমরা __ (double underscore) দিয়ে private variable তৈরি করে এটা করি।
"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks   # private variable

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks


s = Student("Mitu", 90)
print(s.get_marks()) #90
s.set_marks(95)
print(s.get_marks()) #95

# print(s.__marks) # ei vabe sosasori access korte parbo na amra 
#👉 এখানে __marks বাইরের থেকে সরাসরি access করা যায় না। এটাই Encapsulation


"""🎭 2. Abstraction (অ্যাবস্ট্রাকশন) মানে কী?
Abstraction মানে হলো
👉 জটিল জিনিসগুলো লুকিয়ে রাখা, শুধু প্রয়োজনীয় জিনিসগুলো দেখানো।

🔸 যেমন তুমি গাড়ি চালাও —
তুমি জানো স্টার্ট বাটন, ব্রেক, গিয়ার কীভাবে কাজ করে।
কিন্তু ভিতরে ইঞ্জিন কিভাবে ঘোরে বা তেল কিভাবে বার্ন হয় — ওসব জানতে হয় না।

🔸 অর্থাৎ, অপ্রয়োজনীয় details লুকিয়ে রাখা আর মুখ্য বিষয় দেখানোই abstraction।

👉 এখানে Animal class-এ শুধু idea আছে (sound() আছে, কিন্তু body নাই)।
আসল কাজ Dog, Cat class-এ।
এটাই Abstraction — idea define করা, কাজ পরে child class-এ।
"""
""""
#✅ Python উদাহরণ (abstract class দিয়ে):

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog says: Ghew Ghew")

class Cat(Animal):
    def sound(self):
        print("Cat says: Meow Meow")

# obj = Animal()  # Error! Abstract class instantiate করা যায় না
d = Dog()
d.sound()   # Ghew Ghew"""


"""
🔷 Abstraction মানে কী?
অপ্রয়োজনীয় জিনিস লুকিয়ে রাখা, আর প্রয়োজনীয় অংশটা দেখানো — এটাকেই বলে Abstraction।

📱 যেমন: তুমি মোবাইল দিয়ে কাউকে কল দাও —
তুমি শুধু dial বাটন চাপো,
ভিতরে মোবাইল কীভাবে signal পাঠাচ্ছে, call connect করছে — সেগুলো তোমার জানার দরকার হয় না।
🧠 অর্থাৎ, user শুধু দরকারি কাজ দেখে, ভিতরের জটিলতা লুকানো থাকে।
এটাই Abstraction।

🔶 প্রোগ্রামিং-এ Abstraction:
Python-এ Abstraction করতে হলে abstract class আর abstract method ব্যবহার করতে হয়।
"""

from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass  # কোনো কাজ করছে না, শুধু design

# Subclass
class Cow(Animal):
    def sound(self):
        print("Cow says: Hamba")

class Dog(Animal):
    def sound(self):
        print("Dog says: Ghew Ghew")

# Object তৈরি
c = Cow()
c.sound()   # Output: Cow says: Hamba

d = Dog()
d.sound()   # Output: Dog says: Ghew Ghew
"""
🔷 কেন ABC আর abstractmethod দরকার?
Python-এ abstract class তৈরি করতে হলে, আমাদের বলতে হয় —
“এই ক্লাসটা পুরা নয়, এটা শুধু একটা design/template।”
এ জন্য Python-এ একটি মডিউল আছে যার নাম 👉 abc (মানে: Abstract Base Class)


🤔 যদি from abc import না দাও?
তাহলে abstract class বা abstract method কাজই করবে- না। Python বুঝবে না যে তুমি কোনটা design-only আর কোনটা পূর্ণ কাজের method।   
"""