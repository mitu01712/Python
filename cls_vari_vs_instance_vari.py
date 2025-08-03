# Class variable VS Instance Variable 


# Instence Variable
"""
✅ Instance Variable (ইনস্ট্যান্স ভ্যারিয়েবল)
🔹 এটা এমন এক ধরনের ভ্যারিয়েবল,
👉 প্রতিটি object (অথবা instance) আলাদা করে নিজের জন্য রাখে।
🔸 যেটা constructor বা method এর ভেতরে self. দিয়ে লেখা হয়।
"""

# Class Variable
"""✅ Class Variable (ক্লাস ভ্যারিয়েবল)
🔹 এটা এমন একটা ভ্যারিয়েবল,
👉 যেটা সব object মিলে শেয়ার করে।
🔸 এটা __init__ এর বাইরে, সরাসরি ক্লাসের ভিতরে লেখা হয়।"""

class School:
    school_name = "Ostad High School"# class variable

    def __init__(self, name):
        self.student_name = name # eta holo instence variable

sc1 = School("Mitu")
sc2 = School("Satu")
sc1.school_name = "XYZ School"
 # ekhane ekhon sc1 er school name ostad school theke XYZ school print hobe but sc2 er school name change hobe na .

#ekhon amra jodi class variable er value kei change korte chai ,it means amra school name tai change korte chai
School.school_name = "Ghatail High School"

print("School Name:",sc1.school_name)
print("Student Name:",sc1.student_name)

print("School Name:",sc2.school_name,"\n" "Student Name:" ,sc2.student_name)
#new line banate \n use kora hoy
# class variable prottek ta object er jonno common thakbe
# instance variable prottek ta object er jonno alada thakbe

"""
class School:
    school_name = "Ostad High School"  # class variable

    def __init__(self, name):
        self.student_name = name       # instance variable

sc1 = School("Mitu")
sc2 = School("Satu")

sc1.school_name = "XYZ School"   # ✅ এটা একটা নতুন instance variable তৈরি করে sc1 এর জন্য

School.school_name = "Ghatail High School"  # ✅ class variable update করলাম

print("School Name:", sc1.school_name)     # 🔴 instance variable আছে → XYZ School
print("Student Name:", sc1.student_name)

print("School Name:", sc2.school_name)     # 🟢 instance variable নাই → class variable দেখে → Ghatail High School
print("Student Name:", sc2.student_name)
"""

# instance variable এবং class variable একসাথে থাকলে তারা কিভাবে behave করে, এবং কেন instance variable-এর মান class variable পরিবর্তন করলে বদলায় না।
"""
🧠 মৌলিক নিয়ম:
🔹 Class variable: পুরো class-এর জন্য সাধারণ একটা ভ্যারিয়েবল (shared)।
🔹 Instance variable: প্রতিটা object নিজের জন্য আলাদা ভ্যারিয়েবল রাখে।

sc1.school_name তো আগেই instance variable হিসেবে "XYZ School" হয়ে গেছে,
তাই এটা আর class variable এর সাথে সম্পর্ক রাখে না।


"""