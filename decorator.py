# Decorator 

def conversation_decorator(func):
    def wrapper(name):# ruti
        print("Hi Welcome!")# sauce
        func(name)
        print("Bye ! Thanks for the conversation!")
    return wrapper

@conversation_decorator
def greetings(name):# Murgir Gosto
    print(f"Nice to meet you , {name}!")
    print("Awesome!")

greetings(name = "Mitu")

"""output:
Hi Welcome!
Nice to meet you , Mitu!
Awesome!
Bye ! Thanks for the conversation!"""



"""
# এটা হলো একটি ডেকোরেটর ফাংশন
def conversation_decorator(func):  
    # ভিতরে একটা wrapper ফাংশন আছে যেটা মূল ফাংশনের চারপাশে অতিরিক্ত কাজ করে দেয়
    def wrapper(name):  # এখানে 'name' হচ্ছে greetings ফাংশনের প্যারামিটার
        print("Hi Welcome!")  # যেকোনো কথোপকথনের শুরুতে এটা প্রিন্ট হবে
        func(name)            # এখানে আসল ফাংশন (greetings) কল হচ্ছে
        print("Bye ! Thanks for the conversation!")  # কথোপকথনের শেষে এটা প্রিন্ট হবে
    return wrapper  # wrapper ফাংশনটি রিটার্ন করা হচ্ছে, যাতে এটি আসল ফাংশনের জায়গায় কাজ করে

# এই লাইনটি দিয়ে আমরা greetings ফাংশনের উপর ডেকোরেটর প্রয়োগ করছি
@conversation_decorator
def greetings(name):  
    print(f"Nice to meet you , {name}!")  # ইউজারের নাম নিয়ে একটা মেসেজ দেখাচ্ছে
    print("Awesome!")  # আরেকটা সাধারণ বার্তা

# এখন greetings ফাংশনটি কল করা হচ্ছে
greetings(name = "Mitu")

"""

"""

🔍 ব্যাখ্যা:

যখন তুমি greetings(name = "Mitu") কল করো, তখন সরাসরি greetings() ফাংশন কল হয় না।

বরং @conversation_decorator থাকার কারণে greetings এর উপরে conversation_decorator() ফাংশন চালু হয়।

এই conversation_decorator() greetings() কে func হিসেবে নেয় এবং wrapper ফাংশন রিটার্ন করে।

wrapper() যখন কল হয়, তখন সে আগে Hi Welcome! প্রিন্ট করে ➝ তারপর func(name) অর্থাৎ আসল greetings(name) কল করে ➝ তারপর শেষে Bye! Thanks for the conversation! প্রিন্ট করে।

📌 Decorator মূলত ফাংশনের আচরণে অতিরিক্ত ফিচার যোগ করার জন্য ব্যবহৃত হয়, মূল ফাংশনের কোড না বদলিয়ে।
চাইলে আমি আরো রিয়েল লাইফ উদাহরণসহ ডেকোরেটরের ব্যাখ্যাও দিতে পারি।
"""