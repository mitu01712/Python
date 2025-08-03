# Hierarchical and Hybrid Inheritance

# Hierarchical Inheritance
# Multiple sub class ekta parent class ke inherite kore

class Vehicle:
    def engine_type(self):
        print("Vehicle has an engine")

class Car(Vehicle):
    def num_doors(self):
        print("Car has 4 doors")
    
class Truck(Vehicle):
     def load_capacity(self):
         print("Truck can carry 10 tons")

#same class ke jokhon multiple classes inherit kore tokhon amra bolbo hierarchical inheritance.
class Shape:
    def area(self):
        print("Calculating area.....")

class Polygon(Shape):
    def sides(self):
        print("Polygon has multiple sides.")

class Rectangle(Polygon):  
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

# Object creation
rec = Rectangle(10, 5)
rec.sides()  # From Polygon
print(rec.area())  # From Rectangle (overridden method)


"""
🔷 Hierarchical Inheritance
অর্থ: একাধিক child class একটি parent class থেকে inherit করে।

📘 Structure:

        Parent
       /     \
   Child1   Child2
✅ উদাহরণ:

class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
d.sound()  # Output: Animals make sound
d.bark()   # Output: Dog barks

c = Cat()
c.sound()  # Output: Animals make sound
c.meow()   # Output: Cat meows
👉 এখানে Dog এবং Cat দুইটাই Animal কে inherit করেছে। একে বলে Hierarchical Inheritance.

🔷 Hybrid Inheritance
অর্থ: একাধিক inheritance ধরণ একসাথে ব্যবহার করা হলে তাকে Hybrid Inheritance বলে।

✅ উদাহরণ:
এক কোডে যদি Multiple, Multilevel, এবং Hierarchical inheritances একত্রে মেশানো থাকে, সেটি হয় Hybrid।

📘 Structure:

       A
      / \
     B   C
      \ /
       D
✅ কোড উদাহরণ:

class A:
    def method_A(self):
        print("Class A")

class B(A):
    def method_B(self):
        print("Class B")

class C(A):
    def method_C(self):
        print("Class C")

class D(B, C):
    def method_D(self):
        print("Class D")

obj = D()
obj.method_A()  # From A
obj.method_B()  # From B
obj.method_C()  # From C
obj.method_D()  # From D
👉 এখানে আমরা A → B → D, A → C → D — সব একসাথে পাচ্ছি।
এই ধরণের মিশ্র inheritance কে Hybrid Inheritance বলা হয়।

🔄 তুলনা:
Inheritance Type	Structure	Description
Hierarchical	One parent → multiple children	সব child একই parent থেকে inherit করে
Hybrid	Mix of multiple inheritance types	একাধিক inheritance system একত্রে থাকে
"""
