#Methon inside Class
# __init__ () holo build in function
# ekhon amra shikhbo class er vitore kivabe user define function use korte hoy

class Car:
     def __init__(self):# default constructor
        self.brand = ""
        self.model = ""
    
     def __init__(self, brand, model):# parameterize costructor
        self.brand = brand
        self.model = model

     def __init__(self, brand = "Honda", model="Civic"):# default value constructor.
        self.brand = brand
        self.model = model
     def display_info(self):# instance method
         print(f"Car Brand: {self.brand}\n Car Model: {self.model}")
         

car1 = Car("Toyota","Corolla") # constructor er vitor e parametter thakle amra sorasori   
# car1.brand = "Toyota" ekhon amader ekhane pass korar dorkar nai
# car1.model = "Corolla"
# print("Car 1:", car1.brand, car1.model)

car2 = Car()
# car2.brand = "Honda"
# car2.model = "Civic"
# print("Car 2:", car2.brand, car2.model)
car1.display_info()
car2.display_info()

"""
🔶 প্রথমে ক্লাসের সংজ্ঞা:
class Car:
এখানে আমরা Car নামে একটি ক্লাস তৈরি করেছি। ক্লাস হচ্ছে একটি ব্লুপ্রিন্ট, যার মাধ্যমে আমরা object তৈরি করতে পারি।

🔶 Constructor (__init__) ব্যাখ্যা:
def __init__(self, brand = "Honda", model="Civic"):
    self.brand = brand
    self.model = model
❗তিনটি __init__ ফাংশন থাকলেও:
Python-এ method overloading (একই নামে একাধিক constructor) সাপোর্ট করে না।
শেষ __init__ টিই কার্যকর হবে, অর্থাৎ:

def __init__(self, brand = "Honda", model="Civic")
এইটাই রান হবে সব ক্ষেত্রে। অর্থাৎ:
তুমি যদি brand এবং model দুটোই পাঠাও, তাহলে তা সেট হবে।
না পাঠালে default মান "Honda" এবং "Civic" বসে যাবে।

🔶 Instance Method:
def display_info(self):
    print(f"Car Brand: {self.brand}\n Car Model: {self.model}")
এখানে display_info() একটি instance method, যা self.brand ও self.model এর মান প্রিন্ট করে।

🔶 Object তৈরি ও ব্যবহার:
▶ car1 = Car("Toyota", "Corolla")
এখানে আমরা brand="Toyota" এবং model="Corolla" পাঠাচ্ছি, তাই constructor এই ভ্যালুগুলো নেয়:

self.brand = "Toyota"
self.model = "Corolla"
▶ car2 = Car()
এখানে আমরা কিছুই পাঠাচ্ছি না, তাই default constructor কাজ করবে:

self.brand = "Honda"
self.model = "Civic"
🔶 Object Method Call:

car1.display_info()
car2.display_info()
Output:
"""



# ei code ta eivabe likha jay
"""
class Car:
    def __init__(self, brand="Honda", model="Civic"):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car Brand: {self.brand}\nCar Model: {self.model}")

# object তৈরি
car1 = Car("Toyota", "Corolla")  # custom value
car2 = Car()                     # default value

# method call
car1.display_info()
car2.display_info()

"""
