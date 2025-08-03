# Multiple and Multilevel Inheritance

class GrandFather:
    def __init__(self, color, first_name):
        self.color = color
        self.first_name = first_name
    def gf_method(self):
        print("I am from Grandfather")
        

class Father (GrandFather):
    def __init__(self, hobby, color, first_name):
        super().__init__(color, first_name)
        self.hobby = hobby
        print(f"My father's favatite color is {self.color} and his first name is {self.first_name} and his hobby is {self.hobby}")
    def f_method(self):
        print("I am from father")

class Children(Father, GrandFather):
    # ekhon ami father and grandfather er k
    # ono variable nite chaischi na .ami shudu tader method nibo

    def __init__(self, fashion, hobby, color, first_name):
        super().__init__(hobby, color, first_name)
        self.fashion = fashion

# gf1 = GrandFather("red", "Ghosh")
# print("My Grendfather's favarit color",gf1.color, "and his first name was",gf1.first_name)

f1 = Father("Football","Green","Ghosh")
c1 = Children("Test", "Badminton","Red", "Chowdhury")
c1.gf_method()
c1.f_method()
print(c1.fashion)
print(c1.fashion, c1.color, c1.first_name)

#output:I am from Grandfather
# I am from father
# Test
#Test Red Chowdhury

"""
# GrandFather ক্লাস তৈরি করলাম
class GrandFather:
    def __init__(self, color, first_name):
        # Grandfather এর প্রিয় রঙ এবং নাম সেট করলাম
        self.color = color
        self.first_name = first_name

    def gf_method(self):
        # এটা হলো Grandfather এর মেথড
        print("I am from Grandfather")
        

# Father ক্লাস GrandFather থেকে ইনহেরিট করছে
class Father(GrandFather):
    def __init__(self, hobby, color, first_name):
        # GrandFather এর constructor কে call করলাম
        super().__init__(color, first_name)
        # নিজের hobby সেট করলাম
        self.hobby = hobby
        # বাবা সংক্রান্ত তথ্য প্রিন্ট করলাম
        print(f"My father's favatite color is {self.color} and his first name is {self.first_name} and his hobby is {self.hobby}")

    def f_method(self):
        # এটা হলো বাবার method
        print("I am from father")

# Children ক্লাস Father এবং GrandFather দুইটা থেকেই ইনহেরিট করছে
class Children(Father, GrandFather):
    # কিন্তু আমরা বলেছি, Grandfather আর Father এর কোন variables নিচ্ছি না,
    # শুধু method গুলো ব্যবহার করবো

    def __init__(self, fashion, hobby, color, first_name):
        # super() এখানে Father এর constructor কে call করে
        # তাই Father এর মাধ্যমে GrandFather এর constructor ও call হয়ে যাচ্ছে
        super().__init__(hobby, color, first_name)
        # নিজের fashion প্রপার্টি সেট করলাম
        self.fashion = fashion

# Father এর object তৈরি করলাম
f1 = Father("Football", "Green", "Ghosh")

# Children এর object তৈরি করলাম
# এখানে hobby = Badminton, color = Red, first_name = Chowdhury
c1 = Children("Test", "Badminton", "Red", "Chowdhury")

# GrandFather এর method call করলাম
c1.gf_method()

# Father এর method call করলাম
c1.f_method()

# শুধু fashion value print করলাম
print(c1.fashion)

# fashion, color, first_name — তিনটা value একসাথে print করলাম
print(c1.fashion, c1.color, c1.first_name)
"""
