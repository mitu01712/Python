# object toiri korar jei plan ba blue print setakei amra bolchi class
# car class banabo , setar kichu object banabo
# Brand, model, color
class Car:# class er nam obosshoi capital latter er hobe
    def __init__(self):# self diye bujhay ei car class er object ke  indicate kore 
        self.brand = ""
        self.mordel = ""

car1 = Car()
car1.brand = "Toyota"
car1.model = "Corolla"
print("Car 1:", "Brand-Name:", car1.brand,"\n" "Model-Name:", car1.model)

car2 = Car()
car2.brand = "Honda"
car2.model = "Civic"
print("Car 2:","Band-Name:", car2.brand,"\n""Model-Name:", car2.model)


"""
🔷 ১. class কী?
class হলো একটা blueprint বা নকশা, যার মাধ্যমে আমরা object তৈরি করতে পারি।
class Car:
এখানে Car হলো একটা class, যা আমরা পরে ব্যবহার করে অনেক গুলো object তৈরি করতে পারব (যেমন car1, car2 ইত্যাদি)।
👉 নিয়ম অনুযায়ী class-এর নাম Capital letter দিয়ে শুরু হওয়া ভালো (যেমন Car, Student, Person ইত্যাদি)।
"""

"""
🔷 ২. __init__ method
def __init__(self):
    self.brand = ""
    self.model = ""
🔹 __init__() হল একটা special function যাকে constructor বলা হয়।
🔹 যখনই নতুন object তৈরি হবে (car1 = Car()), তখন এই __init__() function টি অটো কল হবে।
🔹 self মানে হচ্ছে এই class দিয়ে তৈরি হওয়া object টি।
➡️ এই লাইনগুলো বলছে:
প্রতিটা Car object এর brand এবং model নামে দুইটা প্রপার্টি থাকবে।
প্রথমে এই গুলোর মান থাকবে ফাঁকা (""), পরে আমরা সেট করতে পারব।
"""

"""
🔷 ৩. Object তৈরি
car1 = Car()
car1.brand = "Toyota"
car1.model = "Corolla"
এখানে car1 হচ্ছে Car class এর একটা object। আমরা এখানে car1 এর brand এবং model সেট করেছি।
"""

"""
🔷 ৫. অন্য object তৈরি করা
car2 = Car()
car2.brand = "Honda"
car2.model = "Civic"
print(car2.brand, car2.model)
এখানে car2 হচ্ছে আরেকটা object। তার brand এবং model আলাদা।
"""
        
      