#Getter and Setter Method
class Employee:
    company_name = "Ostad Company"  # এটা class variable, সব employee এর জন্য common

    def __init__(self, name, salary):
        self.name = name          # public attribute
        self._salary = salary     # protected/private convention অনুযায়ী _ দিয়ে লেখা (though সত্যিকার অর্থে private নয়)

    def get_salary(self, password):
        if password == "admin":           # যদি সঠিক পাসওয়ার্ড দেয়
            print(self._salary)           # তখন salary দেখাবে
        else:
            print("Invalid Access!!!")    # ভুল পাসওয়ার্ড হলে message

    def set_salary(self, password, salary):
        if password == "admin":               # পাসওয়ার্ড মিললে
            self._salary = salary             # নতুন salary সেট করবে
            print(f"New salary:{self._salary}")
        else:
            print("Invalid Access!!!!!")      # ভুল পাসওয়ার্ড হলে কিছুই হবে না

ob1 = Employee("Mitu", "30000")
ob2 = Employee("Karim", "40000")

ob1.get_salary("admin")
ob1.set_salary("admin", 70000)
print(ob1._salary)

"""
class Employee:
    company_name = "Ostad Company"  # এটা class variable, সব employee এর জন্য common

    def __init__(self, name, salary):
        self.name = name          # public attribute
        self._salary = salary     # protected/private convention অনুযায়ী _ দিয়ে লেখা (though সত্যিকার অর্থে private নয়)

    def get_salary(self, password):
        if password == "admin":           # যদি সঠিক পাসওয়ার্ড দেয়
            print(self._salary)           # তখন salary দেখাবে
        else:
            print("Invalid Access!!!")    # ভুল পাসওয়ার্ড হলে message

    def set_salary(self, password, salary):
        if password == "admin":               # পাসওয়ার্ড মিললে
            self._salary = salary             # নতুন salary সেট করবে
            print(f"New salary:{self._salary}")
        else:
            print("Invalid Access!!!!!")      # ভুল পাসওয়ার্ড হলে কিছুই হবে না

"""



"""
✅ Getter এবং Setter Method কী? (সহজ বাংলায় ব্যাখ্যা)
🔷 Getter Method:
Getter method হলো এমন একটি ফাংশন (method), যার কাজ হলো কোনো প্রাইভেট বা গোপন ভ্যারিয়েবল-এর মান পড়া বা দেখানো।

🔹 সাধারণত আমরা Getter method ব্যবহার করি যাতে কেউ সরাসরি কোনো ভ্যারিয়েবল access না করতে পারে — বরং একটা gatekeeper-এর মতো মাধ্যমে ডাটা নেয়।

🔷 Setter Method:
Setter method হলো এমন একটি ফাংশন, যার কাজ হলো কোনো প্রাইভেট ভ্যারিয়েবল-এর মান পরিবর্তন করা, কিন্তু কিছু শর্তের (যেমন পাসওয়ার্ড, ভ্যালিডেশন) ভিত্তিতে।

🔹 এটা নিশ্চিত করে যে কেউ সরাসরি ভ্যারিয়েবলের ভ্যালু না বদলায় — বরং নিয়ম মেনে বদলায়।
🔄 কেন দরকার Getter/Setter?
🔒 Security: sensitive ভ্যালু সরাসরি পরিবর্তন না হোক
🧪 Validation: সঠিক input দিলে তবেই ভ্যালু বদলানো যাবে
🎯 Control: কোন সময় ডাটা দেখানো হবে বা আপডেট হবে তা নিয়ন্ত্রণ করা যায়
"""