# polymorphism --> Method Overriding and Method Overloading

class Animal:
    def make_sound(self):
        print("Some animal sound")
    
class Dog(Animal):
    def make_sound(self):
        print("Dog says: Ghew Ghew")

class Cat(Animal):
    def make_sound(self):
        print("Cat says: Meow Meow")

class Cow(Animal):
    def make_sound(self):
        print("Cow says: Hamba Hamba")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.make_sound()

#output:
# Dog says: Ghew Ghew
# Cat says: Meow Meow
# Cow says: Hamba Hamba

"""
🔶 Polymorphism মানে কী?
Polymorphism = "একটাই জিনিস, অনেক রকম কাজ করতে পারে"
👉 যেমন, তুমি “mobile” শব্দ শুনলে, কারো কাছে সেটা iPhone, কারো কাছে Samsung, কারো কাছে Walton।
একটা নাম → ভিন্ন ভিন্ন রূপে ব্যবহার = Polymorphism



🔷 এখন বুঝি: Method Overriding
Overriding মানে হলো —
Parent ক্লাসে একটা ফাংশন আছে, আর Child ক্লাস সেটা নিজের মতো করে লিখে ফেলে।
👉 যেমন উপরের make_sound() মেথড — সব Child ক্লাস আলাদা আলাদা করে লিখছে।
এটাকে বলে → Method Overriding
⏩ এটা Run-Time Polymorphism।


🔷 Method Overriding:
Method Overriding হয় যখন একটা ছোট ক্লাস (Child class) তার বড় ক্লাসের (Parent class) ফাংশন একই নামে আবার লিখে ফেলে।

মানে, বাবা একটা কাজ করে একভাবে। আর ছেলে একই কাজ করে নিজের মতো করে।
এইভাবে কাজ করাই Overriding।

🔸 এটা হয় যখন Inheritance থাকে।
🔸 একেই বলে Run-Time Polymorphism।
🔸 Python-এ এটা সহজে করা যায়।

🔷 Method Overloading:
Method Overloading হয় যখন একই নামের ফাংশন দিয়ে ভিন্ন ভিন্ন কাজ করা যায়, প্যারামিটার অনুযায়ী।

🔸 যেমন — add() ফাংশনে ২টা সংখ্যা দিলে যোগফল বের করে, আবার ৩টা দিলে তিনটার যোগফল বের করে।

🔸 এটা হয় একই ক্লাসের ভিতরে।
🔸 একেই বলে Compile-Time Polymorphism।
🔸 Python-এ সরাসরি Overloading হয় না, কিন্তু default value বা *args দিয়ে করা যায়।যায়                      |





"""

class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5, 10))      # 15
print(calc.add(2, 3, 4))    # 9
print(calc.add())           # 0
