#Static Method
"""
✅ Static Method কী?
🔹 Static method হল এমন একটি method,
যেটি class-এর ভেতরে লেখা হয়,
কিন্তু সে object (self) বা class (cls) -এর কোনটাকেই ব্যবহার করে না।
🔸 অর্থাৎ —
এই মেথডে self বা cls দরকার হয় না।
শুধু class এর সাথে সম্পর্কিত সাধারণ utility কাজ করে।

✅ Static Method কখন ব্যবহার করব?
🔸 যখন এমন কোনো কাজ থাকে যেটা:
Object বা class-এর property/access লাগবে না
কিন্তু logically class-এর সাথে সম্পর্কিত
🔹 তখন আমরা static method ব্যবহার করি।

✅ কিভাবে লিখব?
🔸 static method লিখতে হয় @staticmethod ডেকোরেটর দিয়ে:
class MyClass:
    @staticmethod
    def greet():
        print("Hello! Welcome.")
🔸 কল করার নিয়ম:

MyClass.greet()      # ক্লাস থেকে কল
obj = MyClass()
obj.greet()          # object থেকেও কল করা যাবে
"""

# another example :

class School:
    school_name = "ABC School"

    @staticmethod
    def calculate_gread(marks):
        if marks>=90:
            return 'A+'
        else:
            return "F"

print(School.calculate_gread(94)) # output:A+
# static method class er kono properties ke access korte pare na
#static method ক্লাসের কোনো properties (অর্থাৎ instance বা class variables) access করতে পারে না।

"""
⛔ এখানে self নেই, তাই:
self.x লেখা যাবে না
cls.x-ও লেখা যাবে না
কারণ static method-এর মধ্যে self বা cls কোনো কিছুর access থাকে না
"""
