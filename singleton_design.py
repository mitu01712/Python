# Singleton Design pattern

#class er ekta matro object thakbe r kono object create kora jabe na
class Singleton:
    _instance = None  # এটা একটি class variable, যেখানে আমরা object সংরক্ষণ করব

    def __new__(cls):
        # __new__ method object তৈরি করার আগেই call হয়
        if cls._instance is None:  # যদি এখনও কোন object তৈরি না হয়
            print("1st object is created")  # প্রথমবার বলবে object তৈরি হয়েছে
            cls._instance = super(Singleton, cls).__new__(cls)  # নতুন object তৈরি করে সেটি _instance এ রাখবে
        return cls._instance  # সবসময় একই object রিটার্ন করবে
ob1 = Singleton()  # এখানে প্রথমবার object তৈরি হবে, "1st object is created" প্রিন্ট হবে
ob2 = Singleton()  # এখানে নতুন করে আর object তৈরি হবে না, আগেরটাই রিটার্ন হবে
print(ob1 is ob2)  # True হবে, কারণ ob1 এবং ob2 একই object কে নির্দেশ করছে

    