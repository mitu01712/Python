# Factory Design pattern

# Step 1: আলাদা আলাদা class বানাই
# 👉 Step 1: প্রথমে ৩টা আলাদা class বানানো হয়েছে

class Car:
    def show(self):
        print("This is a Car.")   # Car object এর show() method

class Bike:
    def show(self):
        print("This is a Bike.")  # Bike object এর show() method

class Truck:
    def show(self):
        print("This is a Truck.")  # Truck object এর show() method
# 👉 Step 2: একটি Factory class বানানো হয়েছে যেটা object তৈরি করবে

class vehicle_factory:
    def get_vehicle(vehicle_type):  # Factory method

        if vehicle_type == "car":
            return Car()       # যদি "car" চাও, Car class এর object return করো
        elif vehicle_type == "bike":
            return Bike()      # যদি "bike" চাও, Bike class এর object return করো
        elif vehicle_type == "truck":
            return Truck()     # যদি "truck" চাও, Truck class এর object return করো
        else:
            return ValueError("Unknown bike")  # অন্য কিছু দিলে Error return করো
# 👉 Step 3: Factory method দিয়ে object তৈরি করো

# Object তৈরি
vehicle1 = vehicle_factory.get_vehicle("car")
vehicle2 = vehicle_factory.get_vehicle("bike")
vehicle3 = vehicle_factory.get_vehicle("truck")

# Method call (print() দিয়ে নয়)
vehicle1.show()
vehicle2.show()
vehicle3.show()

"""
Factory Design Pattern হচ্ছে এমন একটা ডিজাইন প্যাটার্ন যেটা দিয়ে অবজেক্ট তৈরি করার দায়িত্ব আমরা আলাদা একটা ফ্যাক্টরি ক্লাস বা ফাংশনের ওপর ছেড়ে দিই — যাতে ক্লায়েন্ট (user) বুঝতেই না পারে ভিতরে কোন ক্লাসের অবজেক্ট তৈরি হচ্ছে।

🔧 সহজভাবে বললে:
তুমি শুধু বলবে –
"আমাকে একটা Car দরকার" বা "আমাকে একটা Bike দরকার"
Factory তোমার চাহিদা দেখে নিজে থেকেই ঠিক ক্লাসের object তৈরি করে দিবে।
✅ বাস্তব উদাহরণ:
ধরো, তুমি একটা গাড়ির শোরুমে গেছো।

তুমি শুধু বলো:
"আমাকে একটা গাড়ি দিন"
"আমাকে একটা বাইক দিন"
তুমি কোন ব্র্যান্ড, কোন মডেল, কোন ফিচারস — এসব কিছু জানো না। শোরুমের লোক বুঝে শুনে তোমাকে ঠিক object দিয়ে দেয়।
এটাই Factory Pattern।
🔍 কেন দরকার হয়?
অনেকগুলো class থাকলে কাকে কখন ব্যবহার করতে হবে সেটা user-কে জানার দরকার নেই
Code clean, scalable & maintainable হয়
নতুন class যোগ করলে Factory method-এ ১টা লাইন বাড়ালেই হয়ে যায়
Dependency কমায় (loose coupling)
"""
